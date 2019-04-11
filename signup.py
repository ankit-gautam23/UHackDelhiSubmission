#! C:/Users/Ankit/AppData/Local/Programs/Python/Python36-32/python.exe
print("Content-type: text/html")

import datetime
sdate = datetime.datetime.now()

print("""

<!DOCTYPE HTML>

<html>
	<head>
		<title>Fit Yourself-Sign up </title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
        <style>
            form{
                margin:100px;
            }
        </style>
	</head>
	<body class="is-preload">
		<div id="page-wrapper">

			<!-- Header -->
				<header id="header">
					<h1 id="logo"><a href="index.html">Fit Yourself</a></h1>
					<nav id="nav"><ul><li>
""")
print(sdate.strftime("%c"))
print("""
</li><li><a href="login.py" class="button">Log In</a></li>
</nav>
				</header>

		
						<!-- Form -->
							<section>
								<form method="post" action="#">
									<div class="row gtr-uniform gtr-50">
										<div class="col-6 col-12-xsmall">
											<input type="text" name="name" id="name" value="" placeholder="Name" required/>
										</div>
										<div class="col-6 col-12-xsmall">
											<input type="text" name="age" id="age" value="" placeholder="Age" required/>
										</div>
                                        <div class="col-12">
											<select name="gender" id="category" required>
												<option value="">- Gender -</option>
												<option value="Male">Male</option>
												<option value="Female">Female</option>
												<option value="Other">Other</option>
											</select>
										</div>
                                        <div class="col-6 col-12-xsmall">
											<input type="text" name="weight" value="" placeholder="Weight" required/>
										</div>
										<div class="col-6 col-12-xsmall">
											<input type="text" name="mob" id="email" value="" placeholder="Mobile Number" required/>
										</div>
										<div class="col-12">
											<select name="fgoal" id="category" required>
												<option value="">- Fitness Goal -</option>
												<option value="Weight Loss">Weight Loss</option>
												<option value="Weight Gain">Weight Gain</option>							
											</select>
										</div>
                                        <div class="col-12">
											<select name="gpack" id="category" required>
												<option value="">- Gym Pack -</option>
												<option value="1 months">1 months</option>
												<option value="3 months">3 months</option>
												<option value="6 months">6 months</option>
												<option value="1 year">1 Year</option>
											</select>
										</div>
										<div class="col-6 col-12-xlarge" required>
											<input type="password" name="pword" id="password" value="" placeholder="Password" />
										</div>
										
										<div class="col-12">
											<ul class="actions">
												<li><input type="submit" name="btn" value="Register" class="primary" /></li>
											</ul>
										</div>
									</div>
								</form>
							</section>

			<!-- Footer -->
				<footer id="footer">
					<ul class="icons">
						<li><a href="#" class="icon alt fa-twitter"><span class="label">Twitter</span></a></li>
						<li><a href="#" class="icon alt fa-facebook"><span class="label">Facebook</span></a></li>
						<li><a href="#" class="icon alt fa-linkedin"><span class="label">LinkedIn</span></a></li>
						<li><a href="#" class="icon alt fa-instagram"><span class="label">Instagram</span></a></li>
						<li><a href="#" class="icon alt fa-github"><span class="label">GitHub</span></a></li>
						<li><a href="#" class="icon alt fa-envelope"><span class="label">Email</span></a></li>
					</ul>
				</footer>

		</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.dropotron.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>


""")



import cgi, cgitb, MySQLdb
import datetime
db = MySQLdb.connect(host="localhost", user='root',password='kuber', database='gymfit')
curs = db.cursor()
form=cgi.FieldStorage()
cgitb.enable()

date = str(datetime.date.today())

btn = form.getvalue('btn')
if btn != None:
	name = form.getvalue('name')
	age = str(form.getvalue('age'))
	gender = form.getvalue('gender')
	weight = str(form.getvalue('weight'))
	mobile = form.getvalue('mob')
	fgoal = form.getvalue('fgoal')
	gpack = form.getvalue('gpack')
	pword = form.getvalue('pword')
	query = "insert into users values('"+date+"','"+name+"','"+age+"','"+gender+"','"+weight+"','"+mobile+"','"+fgoal+"','"+gpack+"','"+pword+"')"
	print(query)
	res = curs.execute(query)
	print(res)
	if res == 1:
		print("""<html><script>window.alert("Details uploaded Successfully")</script></html>""")
	else:
		print("""<html><script>window.alert("Something went wrong")</script></html>""")