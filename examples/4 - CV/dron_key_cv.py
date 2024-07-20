from kivy.app import App
from kivy.uix.button import Button
import KeyPressModule as KP
from djitellopy import tello
from time import sleep, time
import threading

class TelloApp(App):
    def build(self):
        self.me = tello.Tello()
        self.me.connect()
        print(self.me.get_battery())
        self.battery_thread = threading.Thread(target=self.print_battery_status)
        self.battery_thread.daemon = True
        self.battery_thread.start()
        
        KP.init()
        
        layout = BoxLayout(orientation='vertical')
        self.takeoff_button = Button(text='Take Off')
        self.takeoff_button.bind(on_press=self.takeoff)
        layout.add_widget(self.takeoff_button)
        
        self.land_button = Button(text='Land')
        self.land_button.bind(on_press=self.land)
        layout.add_widget(self.land_button)
        
        return layout

    def takeoff(self, instance):
        self.me.takeoff()

    def land(self, instance):
        self.me.land()

    def print_battery_status(self, interval=3):
        last_battery_check_time = time()
        while True:
            current_time = time()
            if current_time - last_battery_check_time >= interval:
                battery = self.me.get_battery()
                print(f"Battery Status: {battery}%")
                last_battery_check_time = current_time
            sleep(1)

if __name__ == '__main__':
    TelloApp().run()