import graphics as gr
import display as d
import sys
def main(filename):
    myImage = gr.Image(gr.Point(0, 0), filename)
    '''L3: Get the RGB Values at the pixel at x =42 and y = 35'''

    '''This gets the RGB Values at pixel X,Y point (42, 35)'''
    (r,g,b)=myImage.getPixel(42, 35)
    print(r,g,b)



    '''This doubles the Former RGB Values'''
    myImage.setPixel(42, 35, gr.color_rgb(2*r, 2*g, 2*b))
    newRgb=myImage.getPixel(42, 35)
    print(newRgb)

    '''Returns the displayImage function as GraphWin functiosn'''
    screen = d.displayImage(myImage, "Colby College")



    screen.getMouse()

 






if __name__ == '__main__':
    main(sys.argv[1])
    # main(sys.argv[1])
    

