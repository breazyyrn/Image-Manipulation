import graphics as gr
import sys
import display as d
import filters as f
# from filters import filter2, filter3

#contains all the codes for the canvas and filtered images being placed on the canvas 
def main(filename):

    #Creates a zelle image object for the image file
    Img = gr.Image(gr.Point(0, 0), filename)

    #Determines the Width and height according to the width and height and it's double because it's a 2X2 grid
    canvasWidth = Img.getWidth() * 2
    canvasHeight = Img.getHeight() * 2

    #Screen/window to draw the warhol image
    canvas = gr.GraphWin("WARHOL", canvasWidth, canvasHeight)

    ImgList = []

    #appends the sublists of the image list with only the (x, y) coordinate of the top left-corner iamge and beyond
    for x in range(2):
        for y in range(2):
            entry = [x * (canvasWidth/2), y * (canvasHeight/2) ]
            ImgList.append(entry)

    #adds filter name and filterd image to the first sublist
    ImgList[0].append("filter1")
    ImgList[0].append(f.filter1(Img.clone()))


    #adds filter name and filterd image to the second sublist
    ImgList[1].append("filter2")
    ImgList[1].append(f.filter2(Img.clone()))


    #adds filter name and filterd image to the third sublist
    ImgList[2].append("filter3")
    ImgList[2].append(f.filter3(Img.clone()))

    #adds filter name and filterd image to the fourth sublist
    ImgList[3].append("filter4")
    ImgList[3].append(f.filter4(Img.clone()))

    print(ImgList)
    #Places the filtered images in the correct position on the 2X2 warhol grid
    for i in range(len(ImgList)):
        # placeImageInCanvas(canvas, ImgList[i][0], ImgList[i][1], ImgList[i][2], ImgList[i][3])
        placeImageInCanvas(canvas, ImgList[i][3], ImgList[i][0], ImgList[i][1])
       
    #waits for input to close window
    canvas.getMouse()
    canvas.close()


def placeImageInCanvas(canvas, img , topleft_x,topleft_y):

    '''Place the image `img` into the larger canvas `canvas`. The image `img` should be positioned
    so that its top-left corner appears at (row , col) = (topleft_row, topleft_col) in the large canvas.
    NOTE: (0, 0) is the top-left corner.
    Parameters:
    -----------
    canvas: Image. Larger canvas to place the image on.
    img: Image. Image to be placed on the canvas.
    topleft_x: int. x pixel position (column) in `canvas` where the top-left corner of `img` should go
    topleft_y: int. y pixel position (row) in `canvas` where the top-left corner of `img` should go
    '''
    #pass

    #saves the width and height of te given image
    w = img.getWidth()
    h = img.getHeight()


    #Saves the current(x, y) coodinates for the anchor point of the given image in separate variables
    oldX = img.getAnchor().getX()
    oldY = img.getAnchor().getY()


    #Saves where the the (x, y) coordinate of the anchor point of the given image should be to get the corners right
    newX = topleft_x + w/2
    newY = topleft_y + h/2

    #saves the difference between the desired (x, y) coordinate for the anchor and the current anchor point in separate variables.
    dx = newX - oldX
    dy = newY - oldY

    #moves the anchor point of image according to the previous calculated changes in x and y and draws it to the canvas
    img.move(dx, dy)
    img.draw(canvas)
    

if __name__ == "__main__":
    main("flowers.ppm")

    #Prints instructions and exits the program if an incorrect number of command-line arguments are provided
    # if len(sys.argv) != 2:
    #     print("usage: python3 warhol.py <image of imagefile> ")
    #     exit()
    # else:
    #     main(sys.argv[1])