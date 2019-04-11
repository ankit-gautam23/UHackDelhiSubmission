#! C:/Users/Ankit/AppData/Local/Programs/Python/Python36-32/python.exe

print("Content-type: text/html")

import datetime
sdate = datetime.datetime.now()

print("""



<!DOCTYPE HTML>

<html>
	<head>
		<title>Fit Yourself-Sign IN </title>
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
</li><li><a href="signup.py" class="button">Sign Up</a></li>
</nav>
				</header>

		
						<!-- Form -->
							<section>
								<form method="post" action="#">
									<div class="row gtr-uniform gtr-50">
										<div class="col-12-xlarge">
											<input type="text" name="mob" id="mob" value="" placeholder="Enter Mobile Number" required/>
										</div>
										<div class="col-12-xlarge">
											<input type="password" name="pword" id="passwprd" value="" placeholder="Enter Password" required/>
										</div>
										<div class="col-12">
											<ul class="actions">
												<li><input type="submit" name="btn" value="Sign In" class="primary" /></li>
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

btn = form.getvalue('btn')
if btn != None:
    mob = str(form.getvalue('mob'))
    password =form.getvalue('pword')
    query = "select mobile, pword from users where mobile = '"+mob+"' and pword = '"+password+"'"
    print(query)
    res = curs.execute(query)
    if res == 1:
        print("""<html><script>window.location="dashboard.py"</script></html>""")
    else:
        print("""<html><script>window.alert("Worng Credentials")</script></html>""")