# from aiogram.contrib.middlewares.i18n import I18nMiddleware
# from config import I18N_DOMAIN, LOCALES_DIR
# from aiogram import types
# from typing import Tuple, Any


# async def get_lang(user_id):
#     pass
#     # user = await db.get_user(user_id)
#     # if user:
#     #     return user.language

# class ACLMiddleware(I18nMiddleware):
#     async def get_user_locale(self, action: str, args: Tuple[Any]):
#         user = types.User.get_current()
#         return await get_lang(user.id) or user.locale

# def setup_middleware(dp):
#     i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
#     dp.middleware.setup(i18n)
#     return i18n