import requests
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import executor
from config import dp
from reply import menu
from inreply import inmenu2, inmenu,  inmenu3, inmenuA, inmenuB, inmenuF, inmenuJ, inmenuX, inmenuN, inmenuNa, \
    inmenuQa, inmenuQo, inmenuSa, inmenuSi, inmenuSu
import datetime
from datetime import *
# logging.basicConfig(level=logging.INFO)
#
city = "nukus"

url = f"https://dailyprayer.abdulrcs.repl.co/api/{city}"

r = requests.get(url)
print(r.status_code)
res = r.json()
print(res)


@dp.message_handler(Command('start'))
async def start(ms: Message):
    txt = f"<b>Assalomu Alaykum va Raxmatullohu va Barakatuh Mr.{ms.from_user.full_name}! siz bu Botdan Nomoz vaqtlarini Ko'rishingiz mumkin</b>"
    img = open("image/8e7f59399b819d8cd081b529c20c894b.jpg", "rb")
    await ms.answer_photo(img, caption=txt, reply_markup=menu, parse_mode="html")


@dp.message_handler(text="🕰Nomoz Vaqtlari")
async def vaqt(ms: Message):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    await ms.answer_photo(img, reply_markup=inmenu)


@dp.callback_query_handler(text_contains="Toshkent")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Toshkent').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Toshkent shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu2)
    # await call.message.edit_reply_markup(reply_markup=inmenu2)


@dp.callback_query_handler(text_contains="Ertangi")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Toshkent').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Toshkent shahri)</b>ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)
    # await call.message.edit_reply_markup(reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="ortga")
async def ort(call: CallbackQuery):
    img = open("image/8e7f59399b819d8cd081b529c20c894b.jpg", "rb")
    await call.message.answer_photo(img, reply_markup=inmenu)


@dp.callback_query_handler(text_contains="Andijon")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Andijon').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Andijon shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuA)


@dp.callback_query_handler(text_contains="AndijonErtangi")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Andijon').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Andijon shahri)</b>Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Buxoro")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Buxoro').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Buxoro shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuB)


@dp.callback_query_handler(text_contains="MTI")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Buxoro').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Buxoro shahri)</b>Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Farg'ona")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/Farg'ona").json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f"<b>(Farg'ona shahri)</b> namoz vaqti {today}\n\n"
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuF)


@dp.callback_query_handler(text_contains="ONA")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/Farg'ona").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f"<b>(Farg'ona shahri)</b> Ertangi namoz vaqti {today}\n\n"
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Jizzax")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/samarqand').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Jizzax shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuJ)


@dp.callback_query_handler(text_contains="ZAX")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/samarqand').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Jizzax shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Xorazm")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Xorazm').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Xorazm shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuX)


@dp.callback_query_handler(text_contains="ZIM")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Xorazm').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Xorazm shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Namangan")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Namangan').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Namangan shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuN)


@dp.callback_query_handler(text_contains="GAN")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Namangan').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Namangan shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Navoi")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Navoi').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Navoi shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuNa)


@dp.callback_query_handler(text_contains="IY")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Navoi').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Navoi shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Qashqadaryo")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/samarqand').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Qashqadaryo shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuQa)


@dp.callback_query_handler(text_contains="SHI")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/samarqand').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Qashqadaryo shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Qoraqalpog'iston")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/Nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f"<b>(Qoraqalpog'iston shahri)</b> namoz vaqti {today}\n\n"
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuQo)


@dp.callback_query_handler(text_contains="TON")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/Nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f"<b>(Qoraqalpog'iston shahri)</b> Ertangi namoz vaqti {today}\n\n"
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Samarqand")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Samarqand').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Samarqand shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuSa)


@dp.callback_query_handler(text_contains="QAND")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Samarqand').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Samarqand shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Sirdaryo")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Toshkent').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Sirdaryo shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuSi)


@dp.callback_query_handler(text_contains="RYO")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Toshkent').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Sirdaryo shahri)</b> Ertangi namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


@dp.callback_query_handler(text_contains="Surxondaryo")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Buxoro').json()
    bomdod = data['today']["Fajr"]
    quyosh = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Surxondaryo shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenuSu)


@dp.callback_query_handler(text_contains="SUR")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today()
    data = requests.get(f'https://dailyprayer.abdulrcs.repl.co/api/Buxoro').json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.answer_photo(img, f'<b>(Surxondaryo shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', parse_mode='html', reply_markup=inmenu3)


# @dp.message_handler(text="📖Qur'on Tafsiri")
# async def Quron(ms: Message):
#     await ms.answer(f"Mr.{ms.from_user.full_name}! siz bu bo'limda Qur'ondagi To'liq sura yoki Suradan Oyatni qidirishingiz mumkin", reply_markup=quronmenu)


# @dp.callback_query_handler(text_contains="to'liq sura")
# async def quron(call: CallbackQuery):
#     tafsir = "uzb-muhammadsodikmu"
#     # sura = input()
#     url_sura = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}").json()
#     await call.message.edit_text(f'Surani Raqamini Kiriting', url_sura)


if __name__ == "__main__":
    executor.start_polling(dp)


