import discord
from discord.ext import commands
import asyncio

# --- AYARLAR ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!help | SLS Maç Duyuru"))
    print(f"✅ {bot.user.name} Aktif ve Hazır!")

# --- 1. GÜNCEL HELP (YARDIM) KOMUTU (TAM İSTEDİĞİN GİBİ) ---
@bot.command(name="help")
async def help_komutu(ctx):
    embed = discord.Embed(
        title="🤖 SAFESTTAXI10 / SLS BOT YARDIM MENÜSÜ",
        description="Bu bot, Super League Soccer maçlarını duyurmak için tasarlanmıştır. İşte kullanabileceğiniz komutlar:\n",
        color=discord.Color.from_rgb(255, 255, 255)
    )
    
    embed.add_field(
        name="⚽ Maç Duyurusu Yapmak",
        value=(
            "Aşağıdaki formatı kullanarak maç duyurusu yapabilirsiniz. Bu komutu sadece `Mesajları Yönet` yetkisi olanlar kullanabilir.\n\n"
            "**Kullanım Formatı:**\n"
            "`!mac [Saat] [Kod] \"[Takım 1]\" \"[Takım 2]\"` \n\n"
            "**Örnek:**\n"
            "`!mac 21:00 X7B9K2 \"SAFESTTAXI10\" \"Rakipler\"`"
        ),
        inline=False
    )

    embed.add_field(
        name="🏁 Skor Duyurusu Yapmak",
        value=(
            "Maç bittikten sonra sonucu duyurmak için kullanılır.\n\n"
            "**Kullanım Formatı:**\n"
            "`!skor \"[Takım 1]\" [Skor 1] \"[Takım 2]\" [Skor 2]` \n\n"
            "**Örnek:**\n"
            "`!skor \"SAFESTTAXI10\" 3 \"Rakipler\" 1`"
        ),
        inline=False
    )
    
    embed.add_field(
        name="📝 Önemli İpucu:",
        value="Eğer takım isimlerinde boşluk varsa, ismin başına ve sonuna tırnak işareti (`\" \"`) koymayı unutmayın.",
        inline=False
    )
    
    embed.set_footer(text=f"Talep Eden: {ctx.author.name} • SAFESTTAXI10 Bot")
    await ctx.send(embed=embed)

# --- 2. MAÇ DUYURU KOMUTU (YEŞİL TASARIM) ---
@bot.command(name="mac")
@commands.has_permissions(manage_messages=True)
async def mac_duyuru(ctx, saat: str, kod: str, takim1: str, takim2: str):
    embed = discord.Embed(
        title="⚽ SUPER LEAGUE SOCCER - MAÇ DUYURUSU",
        description=f"🔥 **{takim1}** 🆚 **{takim2}** 🔥\n\nKramponları bağlayın, sahaya çıkma vakti geldi!",
        color=discord.Color.from_rgb(46, 204, 113)
    )
    embed.add_field(name="⏰ Maç Saati", value=saat, inline=False)
    embed.add_field(name="🔐 Private Server Kodu", value=kod, inline=False)
    
    avatar_url = ctx.author.avatar.url if ctx.author.avatar else None
    embed.set_footer(text=f"Duyuruyu Yapan: {ctx.author.name} • SAFESTTAXI10", icon_url=avatar_url)
    
    await ctx.send(content="@everyone Maç başlıyor beyler!", embed=embed)
    await ctx.message.delete()

# --- 3. SKOR DUYURU KOMUTU (DESTEK NOTLU) ---
@bot.command(name="skor")
@commands.has_permissions(manage_messages=True)
async def skor_duyuru(ctx, takim1: str, skor1: int, takim2: str, skor2: int):
    embed = discord.Embed(
        title="🏁 MAÇ SONUCU AÇIKLANDI",
        description=f"🏟️ **{takim1}** {skor1}  —  {skor2}  **{takim2}**",
        color=discord.Color.gold()
    )
    sonuc = f"🏆 Kazanan: **{takim1}**" if skor1 > skor2 else (f"🏆 Kazanan: **{takim2}**" if skor2 > skor1 else "🤝 Berabere Bitti!")
    
    embed.add_field(name="⚠️ İletişim & Destek", value="Hata varsa lütfen bu hesapa istek atın: **\"arobloxfan0766\"**", inline=False)
    embed.set_footer(text=f"{sonuc} • SAFESTTAXI10")
    await ctx.send(embed=embed)

# --- 4. HATA YAKALAYICI ---
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("⚠️ **Kanka Dur!** Bu komutu kullanmak için yetkin yok.", delete_after=10)

# --- BURAYA DİKKAT: TOKEN BURAYA EKLENECEK ---
bot.run("")
