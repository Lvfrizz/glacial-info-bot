import discord
from discord.ext import commands
from discord import app_commands
import os

# ==================== CONFIG ====================
TOKEN = os.getenv("DISCORD_TOKEN")          # ← Put your bot token here
GLACIAL_COLOR = 0x7FDBFF               # Light icy blue

# ==================== CONTENT ====================
INFO = {
    "custom_drops": {
        "title": "📦 Custom Drops",
        "description": (
            "**│ White Drops**\n"
            "Full Flak Kit, tools, Kibble and empty Cryopods\n"
            "**✦ White Ring Drops**\n"
            "Same but Higher BP %\n\n"
            "**│ Green Drops**\n"
            "Metal Building Kit\n"
            "**✦ Green Ring Drops**\n"
            "Crafting kit\n\n"
            "**│ Blue Drops**\n"
            "PVP Kit (shotgun, bolas, crossbow, ammo, Rockets)\n"
            "**✦ Blue Ring Drops**\n"
            "Same but Higher BP %\n\n"
            "**│ Purple Drops**\n"
            "Random Dino Saddles\n"
            "**✦ Purple Ring Drops**\n"
            "Same but Higher BP % and Tek saddles\n\n"
            "**│ Yellow Drops**\n"
            "ARB Bullets, Electronics, Silica Pearls\n"
            "**✦ Yellow Ring Drops**\n"
            "Element Shards, Black Pearls, Polymer\n\n"
            "**│ Red Drops**\n"
            "6 Random Chibis, Element\n"
            "**✦ Red Ring Drops**\n"
            "Element, Random Tek Suit piece, Tek Rep"
        )
    },
    "orbital_drops": {
        "title": "🛰️ Orbital Drops",
        "description": (
            "**Blue OSD**\n"
            "Saddles, Tek, Materials, Regular Weapons / BPs\n\n"
            "**Yellow OSD**\n"
            "Saddles, Tek Materials, Flak / Tek\n\n"
            "**Red OSD**\n"
            "Saddles / BPs, Tek / Riot BP%, Materials\n\n"
            "**Purple OSD**\n"
            "Saddles / BPs, Tek / Riot BP%, Materials"
        )
    },
    "modded_crafts": {
        "title": "🛠️ Modded Crafts",
        "description": (
            "**Simplified Recipes:**\n\n"
            "⬩➤ **Cement Paste** → Rocks\n"
            "⬩➤ **Electronics** → Silica Pearls\n"
            "⬩➤ **Gunpowder** → Sparkpowder\n"
            "⬩➤ **Polymer** → Cementing Paste\n"
            "⬩➤ **Sparkpowder** → Cement Paste"
        )
    },
    "bosses": {
        "title": "🦖 Bosses Drops",
        "description": (
            "**Gamma**\n"
            "• Black Pearl: 250-1000\n"
            "• Element: 250-1000\n"
            "• Tek + Metal: 1000-2500\n"
            "• Polymer: 250-1500\n"
            "*(Trophy & Flag included)*\n\n"
            "**Beta**\n"
            "• Black Pearl: 500-1500\n"
            "• Element: 500-1500\n"
            "• Tek + Metal: 1500-3000\n"
            "• Polymer: 500-2000\n"
            "*(Trophy & Flag included)*\n\n"
            "**Alpha**\n"
            "• Black Pearl: 1000-2500\n"
            "• Element: 1000-2500\n"
            "• Tek + Metal: 2500-3500\n"
            "• Polymer: 1000-2500\n"
            "*(Trophy & Flag included)*"
        )
    },
    "mods": {
        "title": "📜 Cluster Mod List",
        "description": (
            "• Helena\n"
            "• Cybers Structures\n"
            "• Pelayoris Cryop Storage\n"
            "• ARKomatic\n"
            "• ASE HatchFrames plus\n"
            "• Just want Cuddles\n"
            "• Tribute and Element transfer\n"
            "• Safe OSD & Element veins\n"
            "• Cheat Prevention\n"
            "• Der Dino Find\n"
            "• Awesome Spy Glass\n"
            "• ASA Bot companion\n"
            "• Tip4Serv Shop Mod\n"
            "• Magas Shop ingame\n"
            "• Solo farm mod\n"
            "• Creature Management tool\n"
            "• White Flag\n"
            "• Automated ARK\n"
            "• Dino Color tokens\n"
            "• World Builder\n"
            "• Helena Bot companion\n"
            "• Automated Dino Wipes\n"
            "• Player Renamer\n"
            "• FPS Bot Booster"
        )
    },
    "stats": {
        "title": "📊 Player & Dino Stats",
        "description": (
            "**Player Stats**\n"
            "• HP = **50x**\n"
            "• Stamina = **50x**\n"
            "• Oxygen = **50x**\n"
            "• Food = Does not go down\n"
            "• Water = Does not go down\n"
            "• Weight = **120x**\n"
            "• Damage = **15x**\n"
            "• Speed = **9x**\n"
            "• Fortitude = **100x**\n"
            "• Crafting = **100000x**\n\n"
            "**Tamed Dino Stats**\n"
            "• HP = **25x**\n"
            "• Stamina = **50x**\n"
            "• Weight = **10000x**\n"
            "• Damage = **15x**\n"
            "• Speed = **1.5x** *(enabled on all flying dinos)*\n\n"
            "**Nerfed Dinos**\n"
            "• Acros\n"
            "• Astrocetus (Space Whale)\n"
            "• Dreadnoughtus\n"
            "• Lumina\n"
            "• Magmasaur\n"
            "• Megachelon\n"
            "• Mek\n"
            "• Umbra"
        )
    }
}

# ==================== SELECT MENU ====================
class GlacialSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Custom Drops", value="custom_drops", emoji="📦", description="White → Red drops + Ring versions"),
            discord.SelectOption(label="Orbital Drops", value="orbital_drops", emoji="🛰️", description="Blue / Yellow / Red / Purple OSDs"),
            discord.SelectOption(label="Modded Crafts", value="modded_crafts", emoji="🛠️", description="Simplified crafting recipes"),
            discord.SelectOption(label="Bosses", value="bosses", emoji="🦖", description="Gamma / Beta / Alpha rewards"),
            discord.SelectOption(label="Mods List", value="mods", emoji="📜", description="Full cluster mod list"),
            discord.SelectOption(label="Player & Dino Stats", value="stats", emoji="📊", description="Player rates + Dino rates + Nerfs"),
        ]
        super().__init__(
            placeholder="Choose a category to view info...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="glacial_ascent_info_select"
        )

    async def callback(self, interaction: discord.Interaction):
        choice = self.values[0]
        data = INFO[choice]

        embed = discord.Embed(
            title=data["title"],
            description=data["description"],
            color=GLACIAL_COLOR
        )
        embed.set_footer(text="Glacial Ascent 50x • Info Panel")
        await interaction.response.send_message(embed=embed, ephemeral=True)


class GlacialInfoView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(GlacialSelect())


# ==================== BOT ====================
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    bot.add_view(GlacialInfoView())
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="setup_panel", description="Post the Glacial Ascent Server Info panel")
@app_commands.checks.has_permissions(administrator=True)
async def setup_panel(interaction: discord.Interaction):
    embed = discord.Embed(
        title="❄️ GLACIAL ASCENT SERVER INFO",
        description=(
            "**INFO UPDATES CONSTANTLY**\n\n"
            "Click the dropdown below to view detailed server information!\n\n"
            "**Maps in Cluster:**\n"
            "The Island • The Center • Ragnarok • Aberration\n"
            "Extinction • Valguero • Astraeos • Lost Colony • Genesis Part 1"
        ),
        color=GLACIAL_COLOR
    )
    embed.set_footer(text="Glacial Ascent 50x • Made for the community")

    await interaction.response.send_message(embed=embed, view=GlacialInfoView())


@setup_panel.error
async def setup_panel_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("You need Administrator permission.", ephemeral=True)
    else:
        await interaction.response.send_message("Something went wrong.", ephemeral=True)


bot.run(TOKEN)