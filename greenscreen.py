import graphics as gr
import display as d
import filters as f

#Shows the greenscreen image and swaps mygreenscreen image with the exotic beach picture.
def main():
    myImage = gr.Image(gr.Point(0, 0), 'myGreenScreen.ppm')
    winW = myImage.getHeight()
    winH = myImage.getWidth()

    #swaps mygreenscreen imgae with the exotic beach ppm.
    newImage = gr.Image(gr.Point(0, 0), 'exotics.ppm')
    f.greenScreen(myImage, newImage)
    win = d.displayImage(myImage, 'myGreenScreen2.ppm')
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()