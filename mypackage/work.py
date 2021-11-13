def m_date():
  from datetime import date

  current_date = date.today()
  t_date = current_date.strftime("%d/%m/%Y")

  print("Сегодня {}".format(t_date))

m_date()
