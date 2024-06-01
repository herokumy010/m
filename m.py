import requests,re
from telebot import TeleBot, types
import json
import time
total_money = 0
good_claims = 0
bad_claims = 0
bot_working = True
admin_id = 5643656889
user = []
userid = []
waletaddres = []
defecult = '0.000708'
TOKEN = "7337084709:AAGSv7GAT-G_lnerCJYEDZXaWVHXUTD_41E"
bot = TeleBot(TOKEN)
import requests

def login(number,num):
    headers = {
        'authority': 'faucetearner.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://faucetearner.org',
        'referer': 'https://faucetearner.org/login.php',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'act': 'login',
    }

    json_data = {
        'email': user[0],
        'password': user[1],
    }

    try:
        response = requests.post('https://faucetearner.org/api.php', params=params, headers=headers, json=json_data)

        if "Login successful" in response.text:
            cookies = response.cookies.get_dict()
            print(cookies)
            print('_' * 60)
            if bot_working:
                if number == 0:
                    bot.send_message(chat_id=admin_id, text=f'Good Login ✅\nin {user[0]}')
                    money(cookies)
                elif number == 1:
                    return allmony(cookies)
                elif number == 2:
                	return widthrowl(cookies,num)
        elif "wrong username or password" in response.text:
            print(f'Bad Login')
            bot.send_message(chat_id=admin_id, text='Bad login ❌')
        else:
            print(f'Error')
            bot.send_message(chat_id=admin_id, text='Error occurred during login')
    except Exception as e:
        print(f'Error: {e}')
        bot.send_message(chat_id=admin_id, text=f'Error: {e}')


def allmony(mtx):
    headers = {
        'authority': 'faucetearner.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'referer': 'https://faucetearner.org/faucet.php',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    response = requests.get('https://faucetearner.org/dashboard.php', cookies=mtx, headers=headers)
    mon = re.findall('<b class="fs-4" translate="no">(.*?) XRP</b>', response.text)[0]
    print(mon)
    return float(mon)


def widthrowl(mtx,mony):
    headers = {
        'authority': 'faucetearner.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://faucetearner.org',
        'referer': 'https://faucetearner.org/withdraw.php',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'act': 'withdraw',
    }

    json_data = {
        'amount': mony,
        'wallet': waletaddres[0],
        'tag': waletaddres[1],
        'eth_address': '0x09685a8781Fa5E55199ff2578215F472E1A937d2',
    }

    response = requests.post('https://faucetearner.org/api.php', params=params, cookies=mtx, headers=headers, json=json_data)
    if 'Due to the large number of withdrawals, the withdrawal time is too long. The number of withdrawals is now changed to once a day. You can continue to earn XRP on our platform and all earnings will be deposited into your personal dashboard. Thank you for your trust and support.' in response.text:
    	msg = 'Bad : Wait 24 h before the next Withdraw .'
    else:
    	msg = f'Successfully Withdraw {mony} . ✅'
    return msg
    
def money(cookies):
    global total_money, good_claims, bad_claims
    while True:
        time.sleep(7)
        if not bot_working:
            bot.send_message(chat_id=admin_id, text='Bot is not working')
            return
        headers = {
            'authority': 'faucetearner.org',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'origin': 'https://faucetearner.org',
            'referer': 'https://faucetearner.org/faucet.php',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'act': 'faucet',
        }
        try:
            response = requests.post('https://faucetearner.org/api.php', params=params, cookies=cookies, headers=headers).text
            if 'Congratulations on receiving' in response:
                good_claims += 1
                json_data = json.loads(response)
                message = json_data["message"]
                start_index = message.find(">") + 1
                end_index = message.find(" ", start_index)
                balance = message[start_index:end_index]
                total_money += float(balance)
                bot.send_message(chat_id=admin_id, text=f"[{good_claims}]Done {balance} XRP£. Total money: {total_money}")
            elif 'You have already claimed, please wait for the next wave!' in response:
                bad_claims += 1
                print(f'[{bad_claims}]Bad Claim With please')
            else:
                print(f'Error')
                bot.send_message(chat_id=admin_id, text='Error occurred during claiming')
        except Exception as e:
            print(f'Error: {e}')
            bot.send_message(chat_id=admin_id, text=f'Error: {e}')

@bot.message_handler(commands=['admin'])
def admin_command(message):
    if message.from_user.id == admin_id:
        keyboard = types.InlineKeyboardMarkup()
        if bot_working:
            status_text = "The bot is working ✅"
            button_text = "Set bot as not working ❌"
        else:
            status_text = "The bot is not working ❌"
            button_text = "Set bot as working ✅"

        keyboard.add(types.InlineKeyboardButton(text=button_text, callback_data='toggle_status'))
        bot.send_message(message.chat.id, status_text, reply_markup=keyboard)
    else:
        pass

@bot.callback_query_handler(func=lambda call: call.data == 'toggle_status')
def toggle_status_callback(call):
    global bot_working
    bot_working = not bot_working
    if bot_working:
        new_status = "The bot is working ✅"
        new_button_text = "Set bot as not working ❌"
    else:
        new_status = "The bot is not working ❌"
        new_button_text = "Set bot as working ✅"

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=new_button_text, callback_data='toggle_status'))
    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=new_status, reply_markup=keyboard)
    except Exception as e:
        print(f'Error: {e}')
        bot.send_message(chat_id=admin_id, text=f'Error: {e}')
        
def xrp_to_usd(xrp_amount):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        conversion_rate = data['ripple']['usd']
        usd_value = xrp_amount * conversion_rate
        
        return usd_value
    except:
        return 'None'
        
        
@bot.message_handler(commands=['details'])
def detail(message):
	try:
		det = (f'Email : {user[0]}\nPass : {user[1]}\nUsername : {userid[0]}\nAddres : {waletaddres[0]}\nTag : {waletaddres[1]}')
		bot.reply_to(message,det)
	except:
		try:
			detl = (f'Email : {user[0]}\nPass : {user[1]}\nUsername : None\nAddres : {waletaddres[0]}\nTag : {waletaddres[1]}')
			bot.reply_to(message,detl)
		except:
			try:
				detl = (f'Email : {user[0]}\nPass : {user[1]}\nUsername : None\nAddres : None \nTag : None')
				bot.reply_to(message,detl)
			except:
				try:
					detl = (f'Email : None\nPass : None\nUsername : None\nAddres : {waletaddres[0]}\nTag : {waletaddres[1]}')
					bot.reply_to(message,detl)
				except:
					bot.reply_to(message,'No details found .')


@bot.message_handler(commands=['withdraw'])
def wid(message):
    chat_id = message.chat.id
    if chat_id != admin_id:
        return
    mut = message.text.split('/withdraw')[1]
    msg = login(2,mut)
    bot.reply_to(message, msg)
@bot.message_handler(commands=['user'])
def add(message):
    chat_id = message.chat.id
    if chat_id != admin_id:
        return
    username = message.text.split('/user')[1]
    userid.append(username)
    msag = (f'User : {userid[0]}\nDone .')
    bot.reply_to(message, msag)
    
@bot.message_handler(commands=['addwalet'])
def addwalit(message):
	chat_id = message.chat.id
	if chat_id != admin_id:
		return
	thetall, theshort = message.text.split('/addwalet')[1].split(':')
	waletaddres.extend([thetall,theshort])
	msg = (f'Addres : {waletaddres[0]}\nTag : {waletaddres[1]}\nThis walet has been added successfully .')
	bot.reply_to(message, msg)
	
@bot.message_handler(commands=['mymony'])
def totalmoney(message):
    chat_id = message.chat.id
    if chat_id != admin_id:
        return
    total_money = login(1,None)
    usd = xrp_to_usd(total_money)
    msg = f"Your Total money : {total_money}\nIn U.S.A dollar : {usd}"
    print(msg)
    bot.reply_to(message, msg)
@bot.message_handler(commands=['add'])
def add(message):
    chat_id = message.chat.id
    if chat_id != admin_id:
        return
    gmail, password = message.text.split('/add')[1].split(':')
    user.extend([gmail, password])
    msg = (f'Email : {user[0]}\nPass : {user[1]}\nThis info has been added successfully .')
    bot.reply_to(message, msg)
@bot.message_handler(commands=['clearinfo'])
def clearinf(message):
	user.clear()
	bot.reply_to(message,'The information has been cleared .')
@bot.message_handler(commands=['mony'])
def money_command(message):
    chat_id = message.chat.id
    if bot_working:
        if chat_id == admin_id:
            try:
            	login(0,None)
            except:
            	bot.reply_to(message,'Enter account with /add email:pass')
        else:
            bot.reply_to(message, 'You are not allowed')
    else:
        bot.send_message(message.chat.id, text='Bot is not working')
bot.infinity_polling()