from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.audio import SoundLoader
sound = SoundLoader.load('minecraft_music.mp3')
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    sound.play()
Config.set('kivy','window_icon','sticker5.png')
index=0
class WinApp(App):
    def build(self):
        global img1
        self.title = 'Arthur18+'
        global layout
        global btnpack
        layout=FloatLayout()
        img=Image(source="qqq.png",pos_hint={"center_x":0.5, "center_y":0.58})
        btnpack=Button(text="СТАРТ",font_size=30,background_color=(1,.5,.5,1),pos_hint={"center_x":0.5, "center_y":0.07},size_hint=(.5, .15), on_press=self.pack)
        layout.add_widget(img)
        layout.add_widget(btnpack)
        return layout

    def pack(self,instance):
        btn=Button(text=" нажимай щоб \nАртур роздівався",font_size=20,background_color=(1,.5,.5,1),pos_hint={"center_x":0.65, "center_y":0.07},size_hint=(.3, .15), on_press=self.f)
        btn1=Button(text=" нажимай щоб \nАртур одівався",font_size=20,background_color=(1,.5,.5,1),pos_hint={"center_x":0.35, "center_y":0.07},size_hint=(.3, .15), on_press=self.f1)
        
        layout.add_widget(btn)
        layout.add_widget(btn1)
        layout.remove_widget(btnpack)
        
    def f(self,instance):
        global index
        if index==0:
            print(index)
            new_img=Image(source="a2.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index +=1
        elif index==1:
            print(index)
            new_img=Image(source="a3.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index +=1
        elif index==2:
            print(index)
            new_img=Image(source="a4.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index +=1
        elif index==3:
            print(index)
            new_img=Image(source="a0.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index +=1
        elif index==4:
            print(index)
            new_img=Image(source="a5.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index +=1
 
    def f1(self,instance):
        global index
        if index==1:
            print(index)
            new_img=Image(source="a1.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index -=1
        elif index==2:
            print(index)
            new_img=Image(source="a2.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index -=1
        elif index==3:
            print(index)
            new_img=Image(source="a3.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index -=1
        elif index==4:
            print(index)
            new_img=Image(source="a4.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index -=1
        elif index==5:
            print(index)
            new_img=Image(source="a0.png",pos_hint={"center_x":0.5, "center_y":0.58})
            layout.add_widget(new_img)
            index -=1





if __name__ == '__main__':
    app=WinApp()
    WinApp().run()
