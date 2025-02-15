from manim import *
class HitoThompson(Scene):
    def construct(self):
        self.buildingVMobject()
    def buildingVMobject(self):
        myRay=VMobject().set_color(TEAL)
        time=0
        myTime=.25
        myDecimal=DecimalNumber(0)
        title=Title('Hacía el descubrimiento de la carga del Electrón')
        my_text=VGroup(Tex('y='),myDecimal,MathTex('\\cdot 10^{-??}'))
        my_text.arrange(RIGHT,buff=0.2)
        VGroup(title,my_text).arrange(DOWN,buff=0.3).to_edge(UP,buff=.5)
        rectangle=SurroundingRectangle(my_text,color=RED)
        my_text.add(rectangle)
        anims=[self.getPlaying(myRay,myTime)]
        self.add(my_text,title)
        while time<7:
            time+=myTime
            myDecimal.add_updater(lambda t: t.set_value(time))
            myRay.set_points_smoothly([LEFT*config['frame_width']/2,ORIGIN,RIGHT*config['frame_width']/2+time*UP/5])
            self.play(*anims)
    def getPlaying(self,ray,timer):
        dot=Dot(radius=0.01).match_color(ray)
        time=0
        return AnimationGroup(
            ShowPassingFlash(ray,run_time=timer,rate_func=lambda t: smooth(t,5),time_width=0.06),
            UpdateFromFunc(dot, lambda m: m.move_to(ray.points[-1]))
        )