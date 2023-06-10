from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret_key'  # Set a secret key for flashing messages

def calculate_discount(purchase_amount, payment_method):
    if payment_method == 'cash':
        return purchase_amount * 0.1
    elif payment_method == 'card':
        return purchase_amount * 0.2
    else:
        return 0

@app.route('/', methods=['GET', 'POST'])
def process_purchase():
    if request.method == 'POST':
        try:
            purchase_amount = float(request.form['purchase_amount'])
            age = int(request.form['age'])
            gender = request.form['gender']
            payment_method = request.form['payment_method']

            if purchase_amount < 1000 or age >= 50:
                flash("Sorry, you are not eligible for the offer.", "error")
            else:
                discount = calculate_discount(purchase_amount, payment_method)

                if gender == 'male':
                    free_item = 'cake'
                elif gender == 'female':
                    free_item = 'chocolate'
                else:
                    flash("Invalid gender entered.", "error")
                    return render_template('index.html')

                payable_amount = purchase_amount - discount
                flash(f"You have qualified for a free {free_item}. Your payable amount is: {payable_amount} taka.", "success")

        except ValueError:
            flash("Invalid input. Please enter valid values.", "error")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
