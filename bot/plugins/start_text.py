#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    Filters,
    Message
)
from bot import (
    AUTH_USERS,
    ONLINE_CHECK_START_TEXT,
    START_OTHER_USERS_TEXT
)


@Client.on_message(
    Filters.command("start") &
    ~Filters.chat(AUTH_USERS)
)
async def num_start_message(client: Client, message: Message):
    await message.reply_text(
        START_OTHER_USERS_TEXT,
        quote=True
    )


@Client.on_message(
    Filters.command("start") &
    Filters.chat(AUTH_USERS)
)
async def nimda_start_message(client: Client, message: Message):
    await message.reply_text(
        ONLINE_CHECK_START_TEXT,
        quote=True
    )