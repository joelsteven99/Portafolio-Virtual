import flet as ft
import requests
from dataclasses import dataclass
@dataclass
class Title:
    t1: str
    t2: str
    def widget(self):
        c1 = ft.Container(content=ft.Text(self.t1), width=220)
        c2 = ft.Container(content=ft.Text(self.t2))
        rw = ft.Row([c1, c2], alignment=ft.MainAxisAlignment.START)
        return rw
@dataclass
class Coin:
    name: str
    current_price: float
    image: str
    def widget(self):
        c1 = ft.Container(content=ft.Text(self.name), width=200)
        c2 = ft.Container(content=ft.Text(str(self.current_price)))
        c3 = ft.Container(content=ft.Image(src=self.image, width=35))
        rw = ft.Row([c3, c1, c2], alignment=ft.MainAxisAlignment.START)
        return rw
def get_data(list_view: ft.ListView):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url).json()
    for item in response:
        coin = Coin(item['name'], item['current_price'], item['image'])
        list_view.controls.append(coin.widget())
def main(page: ft.Page):
    page.title = "CoinSultory"
    page.window_width = 450
    list_view = ft.ListView(expand=True, spacing=10, divider_thickness=4)
    list_view.controls.append(Title("Nombre", "Precio (USD)").widget())
    page.add(list_view)
    get_data(list_view)
    page.update()
ft.app(target=main)