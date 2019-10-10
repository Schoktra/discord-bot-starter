from discord.ext import commands
from discord.commands import ExtensionNotLoaded

class Core(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	@commands.is_owner()
	async def reload(self, ctx, extension):
		user = ctx.message.author
		
		try:
			self.bot.reload_extension(extension)
			await ctx.send(f"{user.name}, {extension} has been reloaded")
		except ExtensionNotLoaded:
			await ctx.send(f"{user.name}, {extension} is not loaded, loading it now.")
			self.bot.load_extension(extension)
			
def setup(bot): bot.add_cog(Core(bot))