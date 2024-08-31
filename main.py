import flet
                  
def fun1(page: flet.Page):
    page.title = "Hormona vitae"
    page.theme = flet.Theme(color_scheme_seed = flet.colors.BLUE_GREY)
    page.bgcolor = "yellow"
#    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    
    def funmini1(e):
        if page.theme == flet.Theme(color_scheme_seed = flet.colors.BLUE_GREY):
            page.theme = flet.Theme(color_scheme_seed = flet.colors.GREEN_ACCENT)
            txt3.value = "Темная тема"
            page.bgcolor = "purple"
            txt10.color = "white"
            txt1.color = "white"
            txt2.color = "white"
            txt3.color = "white"
            num1.color = "white"
        else:
            page.theme = flet.Theme(color_scheme_seed = flet.colors.BLUE_GREY)
            txt3.value = "Светлая тема"
            page.bgcolor = "yellow"
            txt10.color = "dark"
            txt1.color = "dark"
            txt2.color = "dark"
            txt3.color = "dark"
            num1.color = "dark"
        page.update()
    
    def funmini2(e):
        page.clean()
        page.add(flet.Row([bt1, txt1]),
                 flet.Row([num1, txt2, txt3, sc]))
    
    def funmini3(e):
        page.clean()
        page.add(flet.Row([pb],
        alignment = flet.MainAxisAlignment.END),
        flet.Row([]),flet.Row([]),flet.Row([]),flet.Row([]),flet.Row([]),
        flet.Row([img1],alignment = flet.MainAxisAlignment.CENTER),
        flet.Row([txt10],alignment = flet.MainAxisAlignment.CENTER),
        flet.Row([]),flet.Row([]),flet.Row([]),flet.Row([]),
        flet.Row([bt2],alignment = flet.MainAxisAlignment.CENTER),
        flet.Row([bt3],alignment = flet.MainAxisAlignment.CENTER))

    def funmini4(e):
        page.window_close()

    def funmini5(e):
        page.open(ad1)
    
    def funmini6(e):
        page.close(ad1)
    
    def funmini7(e):
        page.open(ad2)

    num1 = flet.Text("1.", size=18, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    
    img1 = flet.Image(src = f"pict\pic3.png", width = 275, height = 275)

    txt1 = flet.Text("                                                              Настройки", size=25, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt2 = flet.Text("Тема -", size=18, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt3 = flet.Text("Светлая тема", size=18, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt4 = flet.Text("Внимание!", size=25, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt5 = flet.Text("Вы дествительно хотите выйти?", size=18, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt6 = flet.Text("О приложении", size=25, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt7 = flet.Text("Hormona vitae V-0.2\n\n     Это приложение создано", size=18, theme_style = flet.TextThemeStyle.LABEL_SMALL)
    txt8 = flet.Text("Начать тест", size=25, theme_style = flet.TextThemeStyle.LABEL_SMALL, color = "white")
    txt9 = flet.Text("Узнать о гормонах", size=25, theme_style = flet.TextThemeStyle.LABEL_SMALL, color = "white")
    txt10 = flet.Text("Hormona vitae", size=25, theme_style = flet.TextThemeStyle.LABEL_SMALL, color = "dark")
    
    bt_yes = flet.FilledButton(text = "Да", on_click=funmini4)
    bt_no = flet.FilledButton(text = "Нет", on_click=funmini6)
    bt1 = flet.IconButton(flet.icons.ARROW_BACK_IOS_NEW, on_click=funmini3, tooltip = "Вернутся в главное меню")
    bt2 = flet.CupertinoFilledButton(content = txt8, width = 400)
    bt3 = flet.CupertinoFilledButton(content = txt9, width = 400)
    
    sc = flet.Switch(on_change = funmini1)
    
    pm1 = flet.PopupMenuItem(text = "Настройки", icon = flet.icons.SETTINGS_OUTLINED, on_click = funmini2)
    pm2 = flet.PopupMenuItem(text = "О приложении", icon = flet.icons.QUIZ_OUTLINED,on_click = funmini7)
    pm3 = flet.PopupMenuItem(text = "Выйти из приложения", icon=flet.icons.EXIT_TO_APP, on_click = funmini5)
    pb = flet.PopupMenuButton(items = [pm1, pm2, pm3], tooltip = "Меню")
    
    ad1 = flet.AlertDialog(modal = True, title = txt4, content = txt5, actions=[bt_yes, bt_no])
    ad2 = flet.AlertDialog(title= txt6, content= txt7)
   
    page.add(flet.Row([pb],
    alignment = flet.MainAxisAlignment.END),
    flet.Row([]),flet.Row([]),flet.Row([]),flet.Row([]),flet.Row([]),
    flet.Row([img1],alignment = flet.MainAxisAlignment.CENTER),
    flet.Row([txt10],alignment = flet.MainAxisAlignment.CENTER),
    flet.Row([]),flet.Row([]),flet.Row([]),flet.Row([]),
    flet.Row([bt2],alignment = flet.MainAxisAlignment.CENTER),
    flet.Row([bt3],alignment = flet.MainAxisAlignment.CENTER))

flet.app(target=fun1, view=flet.AppView.FLET_APP, assets_dir = "assets")
