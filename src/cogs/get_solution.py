from src.cogs.utils.ui import SelectProblemView
from nextcord.ext import commands
from json import load
import nextcord


guild_ids: list[int] = [802568457031778324, 802568457031778324]


class GetSolutionCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=guild_ids)
    async def gethelp(self, interaction: nextcord.Interaction, *, search = "") -> None:
        """
        ::params::
        search =>
            This is the search that is provided,
            the term is then passed into the search
            engine where the algorythem returns an
            id that corisponds to a dict in the
            outline.json file.
            p.s you can also edit this file to hold
            some data that need for the search
            engine.
        """

        search_id = search_fn(search)
        with open("path/to/outline.json", "r") as f:
            json_data: list[dict[str, list[int] | list[str] | int | str]] = load(f)

        for i in json_data:
            if i["id"] == search_id:
                return await ctx.response.send_message(await self.make_solution(i))

        else:
            return await ctx.response.send_message("sorry no stuff found")

    async def make_solution(self, data) -> None:
        ans: str = ""
        with open("run_downs.json", "r") as f:
            data: dict[int, str] = load(f)

        for id_ in data["answers"]:
            ans += data[id_]

        return ans


def setup(bot):
    bot.add_cog(GetSolutionCog(bot))

"""

::CHANGES::
===========

So I have added a system that will ask the user for the problem they are having
and then the bot will respond with the steps to the problem, all the need now is
the search engine, Good luck :)

"""
