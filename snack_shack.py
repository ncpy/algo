limit_sandwich = 45
limit_potato = 30

make_sandwich   = 60 #sec
serve_sandwich  = 30

put_pototo_mw   = 1 
heat_potato     = 150  #it can wait at microwave (my point)
top_potato      = 30 
serve_potato    = 30

#variable
order_sandwich = 1
order_potato = 1

time = 0
def make_serve(order_sandwich, order_potato, time):
    k = order_potato

    while order_sandwich > 0:
        time += make_sandwich + serve_sandwich
        order_sandwich -= 1
    
    while order_potato > 0:
        #1.durum, 2 iptal
        if time < heat_potato*k:
            time = put_pototo_mw + heat_potato
            time += top_potato + serve_potato
        else:
            time += put_pototo_mw + top_potato + serve_potato + heat_potato

        # 2. durum, 1 iptal
        # time += put_pototo_mw + top_potato + serve_potato + heat_potato    
        order_potato -= 1

    return time

time = make_serve(order_sandwich, order_potato, time)
print(order_sandwich, "sandwich + ", order_potato, "potato ", "in ", time, " seconds")