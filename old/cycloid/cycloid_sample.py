from manimlib.imports import *
import numpy
#class Intro(Scene):
    #def construct(self):


class Cycloid1(Scene):
    CONFIG = {"camera_config":{"background_color": WHITE}}
    def construct(self):
        coor = NumberPlane()
        label_x = coor.get_x_axis_label("x").set_color(GREY)
        label_y = coor.get_y_axis_label("y").set_color(GREY)
        circle_1 = Circle(radius=1,color=LIGHT_GREY)
        circle_1.shift(UP)
        t = ValueTracker(value=0)
        dot = Dot(color=ORANGE)
        text_1 = TextMobject("我们画一个单位圆").shift(DOWN*3).set_color(BLACK)
        text_2 = TextMobject("把它放在坐标系中").shift(DOWN * 3).set_color(BLACK).add_background_rectangle(color=WHITE,opacity=1)
        self.play(Write(text_1),ShowCreation(circle_1),FadeInFromLarge(dot))
        self.wait()
        self.play(FadeOut(text_1))
        self.play(Write(text_2))
        self.wait()
        circle_and_dot = VGroup(circle_1,dot)
        self.play(ShowCreation(coor),FadeIn(label_x),FadeIn(label_y))
        self.wait()
        self.play(FadeOut(circle_1),FadeOut(dot))
        dot.add_updater(lambda m: m.set_x(t.get_value() - np.sin(t.get_value()) ))
        dot.add_updater(lambda m: m.set_y(1 - np.cos(t.get_value())))
        circle_1.add_updater(lambda m: m.set_x(t.get_value()))
        t.increment_value(-9)
        self.add(circle_1,dot)
        self.play(FadeOut(text_2))
        func_1 = ParametricFunction(lambda m:np.array([m-np.sin(m),1-np.cos(m),0]),t_min=-9,t_max=12)
        func_1.set_color(ORANGE)
        text_3 = TextMobject("描出圆上一点的轨迹").shift(DOWN * 3).set_color(BLACK).add_background_rectangle(color=WHITE,opacity=1)
        text_4 = TextMobject("橙色","的轨迹即为摆线").shift(DOWN * 3).set_color(BLACK).add_background_rectangle(color=WHITE,opacity=1)
        text_4[1].set_color(ORANGE)
        self.play(Write(text_3))
        self.play(ShowCreation(func_1),ApplyMethod(t.increment_value,21),run_time=6,rate_func=linear)
        self.play(FadeOut(text_3))
        self.play(Write(text_4))
        self.wait(2)
        # 背景坐标系遮住了圆的线条
        cycloid_and_coor = VGroup(coor,func_1)
        circle_and_dot.remove()
        self.play(FadeOut(text_4))
        self.play(ApplyMethod(cycloid_and_coor.shift,UP+LEFT*4),ApplyMethod(label_y.shift,LEFT*4),ApplyMethod(label_x.shift,UP))
        text_box = Rectangle().set_width(9).set_height(4).set_fill(color=DOUBLE_LIGHT_GREY,opacity=0.8).set_stroke(color=DARK_GREY,width=1)
        text_box.move_to(np.array([1.5,-1.5,0]))
        self.play(FadeInFromPoint(text_box,np.array([1.5,-1.5,0])))
        text_5 = TextMobject("1、","摆","线","的","参","数","方","程").scale(0.8).next_to(text_box,UP).align_to(text_box,LEFT).shift(DOWN+RIGHT*0.5).set_color(BLACK)
        text_5[0].set_color(ORANGE)
        self.wait()
        self.play(FadeInFrom(text_5[0], UP), FadeInFrom(text_5[1], DOWN),
                  FadeInFrom(text_5[2], UP), FadeInFrom(text_5[3], DOWN),
                  FadeInFrom(text_5[4], UP), FadeInFrom(text_5[5], DOWN),
                  FadeInFrom(text_5[6], UP), FadeInFrom(text_5[7], DOWN))
        circle_2 = Circle(radius=1,color=LIGHT_GREY)
        circle_2.move_to(LEFT+UP*2)
        dot_2 = Dot(color=ORANGE).move_to(LEFT+UP*3)
        circle_and_dot_2 = VGroup(circle_2,dot_2)
        self.play(FadeInFrom(circle_and_dot_2,UP))
        vector_1 = coor.get_vector(np.array([3,2,0])).set_color(BLUE)
        self.play(FadeInFromLarge(vector_1))
        t_1 = ValueTracker(3)
        circle_2.add_updater(lambda m:m.set_x(t_1.get_value() - 4))
        dot_2.add_updater(lambda m:m.set_x(t_1.get_value() - np.sin(t_1.get_value()) - 4)).add_updater(lambda m:m.set_y(2 - np.cos(t_1.get_value())))
        vector_1.add_updater(lambda m:m.put_start_and_end_on(np.array([-4,1,0]),dot_2.get_center()))
        self.wait()
        self.play(ApplyMethod(t_1.increment_value,2*PI),run_time=3)
        label_u = TexMobject("\overrightarrow{u}").set_color(BLUE).next_to(text_5,DOWN*1.2).align_to(text_5,LEFT)
        vector_1_copy = vector_1.copy()
        vector_1_copy.clear_updaters()
        self.play(Transform(vector_1_copy,label_u))
        self.play(ApplyMethod(t_1.increment_value, -2 * PI), run_time=3)
        vector_2 = coor.get_vector(np.array([0,1,0])).set_color(RED)
        vector_3 = Vector(np.array([3,0,0])).set_color(GREEN)
        vector_3.move_to(np.array([-2.5,2,0]))
        vector_4 = Vector(np.array([0,1,0])).set_color(PURPLE)
        vector_4.move_to([-1,2.5,0])
        equal_tex = TextMobject("=").set_color(BLACK).next_to(label_u,RIGHT)
        label_vector = TexMobject("\overrightarrow{u_{1}}","+","\overrightarrow{u_{2}}","+","\overrightarrow{u_{3}}")
        label_vector[0].set_color(RED)
        label_vector[2].set_color(GREEN)
        label_vector[4].set_color(PURPLE)
        label_vector.next_to(equal_tex,RIGHT)
        label_vector[1].set_color(BLACK)
        label_vector[3].set_color(BLACK)
        self.play(FadeInFromLarge(equal_tex))
        self.play(ShowCreation(vector_2))
        self.play(TransformFromCopy(vector_2,label_vector[0]))
        self.play(ShowCreation(vector_3))
        self.play(Write(label_vector[1]),TransformFromCopy(vector_3, label_vector[2]))
        self.play(ShowCreation(vector_4))
        self.play(Write(label_vector[3]), TransformFromCopy(vector_4, label_vector[4]))
        self.wait(3)
        self.play(FadeOut(vector_1))
        vector_3.add_updater(lambda m:m.put_start_and_end_on(np.array([-4,2,0]),circle_2.get_center()))
        vector_4.add_updater(lambda m:m.put_start_and_end_on(circle_2.get_center(),dot_2.get_center()))
        self.play(ApplyMethod(t_1.increment_value,6),run_time=3)
        self.wait(0.75)
        self.play(ApplyMethod(t_1.increment_value,-8),run_time=3.25)
        self.wait(0.5)
        label_radius = TexMobject("r").set_color(BLACK).scale(0.6).move_to(np.array([-2.8,1.5,0]))
        assist_line = DashedLine(start=np.array([-3, 2, 0]), end=np.array([-3, 1, 0])).set_color(BLACK)
        self.play(FadeInFromLarge(label_radius),ShowCreation(assist_line))
        self.wait()
        text_6 = TextMobject("易知","$\overrightarrow{u_{1}}$","=","$(0,r)$").scale(0.6)
        text_6[0].set_color(BLACK)
        text_6[1].set_color(RED)
        text_6[2].set_color(BLACK)
        text_6[3].set_color(BLACK)
        text_6.next_to(label_u,DOWN*1.2).align_to(label_u,LEFT)
        self.play(Write(text_6))
        arc_1 = ArcBetweenPoints(np.array([-3.25,1.8,0]),np.array([-3,1.5,0]),1).set_color(BLACK)
        label_t = TexMobject("t").set_color(BLACK).scale(0.8).next_to(arc_1,DL*0.1)
        text_t = TextMobject("设","$\overrightarrow{u_{3}}$","转过的弧度为t").scale(0.6).set_color(BLACK)
        text_t[1].set_color(PURPLE)
        text_t.next_to(text_6,RIGHT)
        self.wait()
        self.play(Write(text_t))
        self.wait()
        self.play(FadeInFromLarge(arc_1),TransformFromCopy(text_t[2],label_t))
        text_7 = TextMobject("经观察可知","$\overrightarrow{u_{3}}$","转过的","弧长","恰好与圆心移动的","路程","相等").set_color(BLACK).scale(0.6)
        text_7[1].set_color(PURPLE)
        text_7[3].set_color(PURPLE)
        text_7[5].set_color(GREEN)
        text_7.next_to(text_6,DOWN*1.2).align_to(text_6,LEFT)
        arc_2 = ArcBetweenPoints(dot_2.get_center(),np.array([-3,1,0]),1).set_color(PURPLE)
        line_1 = Line(start=np.array([-4,1,0]),end=np.array([-3,1,0])).set_color(GREEN)
        self.play(Write(text_7[0]))
        self.wait(0.5)
        self.play(Write(text_7[1:4]),run_time=3)
        self.play(WiggleOutThenIn(text_7[3]))
        self.play(TransformFromCopy(text_7[3],arc_2))
        self.wait(0.5)
        self.play(WiggleOutThenIn(arc_2))
        self.wait(0.5)
        self.play(Write(text_7[4:7]),run_time=4)
        self.play(WiggleOutThenIn(text_7[5]))
        self.play(TransformFromCopy(text_7[5],line_1))
        label_rt = TexMobject("rt").scale(0.6).set_color(BLACK).next_to(line_1,DOWN*0.5)
        self.wait(0.5)
        self.play(FadeInFromLarge(label_rt))
        self.wait(0.5)
        self.play(WiggleOutThenIn(line_1))
        self.wait(2)
        text_8 = TextMobject("于是有","$\overrightarrow{u_{2}}$","=(rt,0)",",","$\overrightarrow{u_{3}}$","$=(-r \sin t, - \cos t)$").scale(0.6).set_color(BLACK)
        text_8[1].set_color(GREEN)
        text_8[4].set_color(PURPLE)
        text_8.next_to(text_7,DOWN*1.2).align_to(text_7,LEFT)
        self.play(Write(text_8[0:4]),run_time=3)
        self.wait(0.5)
        self.play(Write(text_8[4:6]),run_time=3)
        self.wait()
        text_9 = TextMobject("$\Rightarrow \\begin{cases}x = r(t-\\sin t)\\\\y = r(1 - \\cos t)\\end{cases}$").set_color(BLACK).scale(0.6)
        text_9.next_to(label_vector,RIGHT*0.8)
        self.play(Write(text_9),run_time=3)
        self.play(ApplyWave(text_9))
        self.wait(3)

class Cycloid2(Scene):
    CONFIG = {"camera_config": {"background_color": WHITE}}
    def construct(self):
        coor = NumberPlane().shift(DOWN*2)
        label_x = coor.get_x_axis_label("x").set_color(GREY)
        label_y = coor.get_y_axis_label("y").set_color(GREY)
        origin = Dot(ORIGIN).set_color(LIGHT_GREY)
        text_box = Rectangle().set_width(4,stretch=True).set_height(1,stretch=True).set_fill(color=DOUBLE_LIGHT_GREY,opacity=0.8).set_stroke(color=DARK_GREY,width=1)
        text_box.move_to(np.array([-5,3,0]))
        title = TextMobject("2、","摆","线","运","动","的","速","率").scale(0.8).move_to(text_box.get_center()).set_color(BLACK)
        title[0].set_color(ORANGE)
        self.play(FadeInFromPoint(text_box, np.array([-6,2.5, 0])))
        self.play(FadeInFrom(title[0], UP), FadeInFrom(title[1], DOWN),
                  FadeInFrom(title[2], UP), FadeInFrom(title[3], DOWN),
                  FadeInFrom(title[4], UP), FadeInFrom(title[5], DOWN),
                  FadeInFrom(title[6], UP), FadeInFrom(title[7], DOWN))
        self.wait()
        text_0 = TextMobject("按照惯例，先画圆").set_color(BLACK)
        text_0.add_background_rectangle(color=WHITE).shift(DOWN*3)
        circle_1 = Circle(radius=2,color=LIGHT_GREY)
        circle_1.move_to(ORIGIN)
        dot_1 = Dot(color=ORANGE)
        dot_1.move_to(np.array([-1,np.sqrt(3),0]))
        self.play(Write(text_0))
        self.play(ShowCreation(circle_1),FadeInFromLarge(dot_1),FadeIn(origin))
        radius_line = DashedLine(start=circle_1.get_center(),end=dot_1.get_center()).set_color(LIGHT_GREY)
        radius = TexMobject("r").set_color(BLACK).move_to(np.array([-0.4,1.2,0]))
        self.play(ShowCreation(radius_line),FadeInFromDown(radius))
        vector_velocity_1 = Vector(np.array([np.sqrt(3),1,0]),color=PURPLE)
        vector_velocity_2  = Vector(np.array([2,0,0]),color=GREEN)
        vector_velocity_1.put_start_and_end_on(np.array([-1,np.sqrt(3),0]),np.array([np.sqrt(3)-1,1+np.sqrt(3),0]))
        self.wait()
        text_1 = TextMobject("圆周旋转的线速度").set_color(PURPLE).scale(0.6)
        text_2 = TextMobject("圆心平动的速度").set_color(GREEN).scale(0.5)
        text_1.move_to(np.array([-0.3,1.8+np.sqrt(3)/2,0])).rotate(PI/6)
        text_2.move_to(np.array([1,0.4,0]))
        text_3 = TextMobject("圆上一点的速度可以分解为","$u_{1}$","和","$u_{2}$").set_color(BLACK).shift(DOWN*3)
        text_3[1].set_color(PURPLE)
        text_3[3].set_color(GREEN)
        text_3.add_background_rectangle(color=WHITE)
        self.play(FadeOut(text_0))
        self.play(Write(text_3[1]))
        self.play(FadeInFromDown(text_3[2]))
        self.wait(0.5)
        self.play(TransformFromCopy(text_3[2],vector_velocity_1),Write(text_1))
        self.wait()
        self.play(Write(text_3[3]))
        self.play(FadeInFromDown(text_3[4]))
        self.wait(0.5)
        self.play(TransformFromCopy(text_3[4],vector_velocity_2))
        self.play(Write(text_2))
        text_2_vector2_group = Group(text_2,vector_velocity_2)
        self.wait(2)
        self.play(FadeOut(text_3))
        text_4 = TextMobject("将两向量首尾相连").set_color(BLACK).shift(DOWN*3)
        text_4.add_background_rectangle(color=WHITE)
        self.play(Write(text_4))
        self.wait(0.5)
        self.play(ApplyMethod(text_2_vector2_group.shift,UP*(1+np.sqrt(3))+RIGHT*(np.sqrt(3)-1)))
        self.wait()
        vector_velocity_3 = Vector().put_start_and_end_on(dot_1.get_center(),np.array([1+np.sqrt(3),1+np.sqrt(3),0])).set_color(BLUE)
        self.play(ShowCreation(vector_velocity_3))
        vector_group = Group(vector_velocity_1,vector_velocity_2,vector_velocity_3,text_1,text_2)
        self.wait()
        text_5 = TextMobject("根据我们的选择","$u_{1}$","和","$u_{2}$","的长度都等于单位长度").set_color(BLACK).shift(DOWN*3)
        text_5[1].set_color(PURPLE)
        text_5[3].set_color(GREEN)
        text_5.add_background_rectangle(color=WHITE)
        text_6 = TextMobject("*圆的半径r也为单位长度").set_color(BLACK).add_background_rectangle(WHITE).scale(0.4).move_to(np.array([3,1,0]))
        self.play(FadeOut(text_4))
        self.play(Write(text_5),run_time=2)
        self.add(text_6)
        self.wait(2)
        self.remove(text_6)
        self.play(FadeOut(text_5))
        text_7 = TextMobject("将三个向量顺时针旋转","$90^{\circ}$").set_color(BLACK).add_background_rectangle(WHITE).shift(DOWN*3)
        self.play(Write(text_7))
        self.wait(0.5)
        self.play(Rotate(vector_group,-PI/2,about_point=np.array([-1,np.sqrt(3),0])))
        dash_line_1  = DashedLine(start=np.array([0,-2,0]),end=dot_1.get_center()).set_color(BLUE)
        self.play(FadeOut(vector_velocity_1),FadeOut(vector_velocity_2),FadeOut(text_1),FadeOut(text_2),FadeOut(text_7))
        self.wait(0.5)
        text_8 = TextMobject("我们发现，这一点运动的速度变成了圆的弦").set_color(BLACK).add_background_rectangle(WHITE).shift(DOWN*3)
        self.play(Write(text_8))
        self.wait(2)
        text_9 = TextMobject("它将运动的这一点与","圆和地面的交点","连接了起来").set_color(BLACK).add_background_rectangle(WHITE).shift(DOWN*3)
        dot_2 = Dot(np.array([0,-2,0])).set_color(BLUE)
        text_9[2].set_color(BLUE)
        self.play(FadeOut(text_8))
        self.play(Write(text_9))
        self.play(TransformFromCopy(text_9[2],dot_2))
        self.wait()
        text_10 = TextMobject("换句话说，我们可以将这一点的运动速度简单地当成一条在旋转的弦").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).shift(DOWN*3)
        self.play(FadeOut(text_9))
        self.play(Write(text_10))
        self.wait(0.5)
        self.play(TransformFromCopy(vector_velocity_3,dash_line_1),Rotate(vector_velocity_3,PI/2,about_point=dot_1.get_center()))
        self.wait()
        self.play(FadeOut(radius),FadeOut(radius_line))
        self.play(ShowCreation(coor),FadeIn(label_x),FadeIn(label_y))
        self.add(text_10,text_box,title)
        self.wait()
        curve_1 = ParametricFunction(lambda m:np.array([2*m-2*np.sin(m),-2*np.cos(m),0]),t_min=-PI,t_max=-(2/3)*PI).set_color(ORANGE)
        self.play(FadeOut(circle_1),FadeOut(dash_line_1),FadeOut(dot_1),FadeOut(dot_2),FadeOut(origin),FadeOut(vector_velocity_3))
        t = ValueTracker(-PI)
        circle_1.add_updater(lambda m:m.set_x(t.get_value()*2))
        dot_1.add_updater(lambda m:m.set_x(2*t.get_value()-2*np.sin(t.get_value()))).add_updater(lambda m:m.set_y(-2*np.cos(t.get_value())))
        dash_line_1.add_updater(lambda m:m.put_start_and_end_on(circle_1.get_center()+DOWN*2,dot_1.get_center()))
        vector_velocity_3.add_updater(lambda m:m.put_start_and_end_on(dot_1.get_center(),dot_1.get_center()+np.array([2-2*np.cos(t.get_value()),2*np.sin(t.get_value()),0])))
        self.play(FadeIn(circle_1),FadeIn(dot_1),FadeIn(dash_line_1),FadeIn(vector_velocity_3))
        self.wait()
        vector_3_1 = vector_velocity_3.copy().clear_updaters()
        dash_line_1_1 = dash_line_1.copy().clear_updaters()
        self.add(vector_3_1,dash_line_1_1)
        self.play(ShowCreation(curve_1),ApplyMethod(t.increment_value,(1/3)*PI),run_time=1.5,rate_func=linear)
        vector_3_2 = vector_velocity_3.copy().clear_updaters()
        dash_line_1_2 = dash_line_1.copy().clear_updaters()
        self.add(vector_3_2,dash_line_1_2)
        curve_2 = ParametricFunction(lambda m: np.array([2 * m - 2 * np.sin(m), -2 * np.cos(m), 0]), t_min=-(2/3)*PI,
                                     t_max=-(1/3)*PI).set_color(ORANGE)
        self.play(ShowCreation(curve_2),ApplyMethod(t.increment_value,(1/3)*PI),run_time=1.5,rate_func=linear)
        vector_3_3 = vector_velocity_3.copy().clear_updaters()
        dash_line_1_3 = dash_line_1.copy().clear_updaters()
        self.add(vector_3_3,dash_line_1_3)
        curve_3 = ParametricFunction(lambda m: np.array([2 * m - 2 * np.sin(m), -2 * np.cos(m), 0]), t_min=-(1/3)*PI,
                                     t_max=(1/3)*PI).set_color(ORANGE)
        self.play(ShowCreation(curve_3),ApplyMethod(t.increment_value,(2/3)*PI),run_time=3,rate_func=linear)
        vector_3_4 = vector_velocity_3.copy().clear_updaters()
        dash_line_1_4 = dash_line_1.copy().clear_updaters()
        self.add(vector_3_4,dash_line_1_4)
        curve_4 = ParametricFunction(lambda m: np.array([2 * m - 2 * np.sin(m), -2 * np.cos(m), 0]), t_min=(1/3)*PI,
                                     t_max=(2/3)*PI).set_color(ORANGE)
        self.play(ShowCreation(curve_4), ApplyMethod(t.increment_value, (1 / 3) * PI), run_time=1.5, rate_func=linear)
        vector_3_5 = vector_velocity_3.copy().clear_updaters()
        dash_line_1_5 = dash_line_1.copy().clear_updaters()
        self.add(vector_3_5,dash_line_1_5)
        curve_5 = ParametricFunction(lambda m: np.array([2 * m - 2 * np.sin(m), -2 * np.cos(m), 0]), t_min=(2 / 3) * PI,
                                     t_max=PI).set_color(ORANGE)
        self.play(ShowCreation(curve_5), ApplyMethod(t.increment_value, (1 / 3) * PI), run_time=1.5, rate_func=linear)
        vector_3_6 = vector_velocity_3.copy().clear_updaters()
        dash_line_1_6 = dash_line_1.copy().clear_updaters()
        self.add(vector_3_6,dash_line_1_6)
        text_11 = TextMobject("速度的大小时刻与弦长相等").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).shift(DOWN*3)
        self.play(FadeOut(text_10))
        self.play(Write(text_11))
        self.wait(2)
        text_12 = TextMobject("一通计算猛如虎,我们最终得到:").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).shift(DOWN*3)
        self.play(FadeOut(text_11))
        self.play(Write(text_12))
        self.play(ApplyMethod(text_12.shift,LEFT*4))
        text_13 = TextMobject("u=","$r\sqrt{2-2\cos t}$","也可以表示为","$2r\sin \\frac{t}{2}$").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).next_to(text_12,RIGHT)
        text_13[2].set_color(RED)
        text_13[4].set_color(RED)
        self.play(FadeInFromPoint(text_13,text_13.get_center()))
        self.wait(5)
        self.play(FadeOut(text_13),FadeOut(text_12))
        text_14 = TextMobject("顺便说一下，这里我们不经意间发现了圆的弦长公式").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).shift(DOWN*3)
        text_15 = TextMobject("即如果半径为r的圆上两点之间的圆心角为t").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).shift(DOWN*3)
        text_16 = TextMobject("那么连接这两点的弦的长度为","$r\sqrt{2-2\cos t}$").set_color(BLACK).add_background_rectangle(WHITE).scale(0.8).shift(DOWN*3)
        text_16[2].set_color(RED)
        self.play(Write(text_14))
        self.wait(2)
        self.play(FadeOut(text_14))
        self.play(Write(text_15))
        self.wait(2)
        self.play(FadeOut(text_15))
        self.play(Write(text_16))
        self.wait(4)
