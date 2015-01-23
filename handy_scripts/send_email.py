# Import smtplib for the actual sending function
import smtplib

smtp = smtplib.SMTP('localhost')
smtp.sendmail('me@worldofsoka.in', 'siddharthmanu@gmail.com', "heyy")
smtp.close()
