from tkinter.constants import W
import graphics as gr
import display as d
import sys
import filters as f
'''Swaps the green and blue values of every pixel of a Zelle image `img`'''
def swapGreenBlue(img):
    '''Swaps the green and blue values of every pixel of a Zelle image `img`'''
    '''For x in range width and height is basically the rows and columns in other word its how u cover the whole image'''
    for x in range(img.getWidth()):
        for y in range(img.getWidth()):
            (r,g,b) = img.getPixel(x, y)
            img.setPixel(gr.Point(0,0), gr.color_rgb(r, b, g))
    return img


def filter1(img):
    '''For x in range width and height is basically the rows and columns in other word its how u cover the whole image'''
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            (r, g, b) = img.getPixel(x, y)
            img.setPixel(x, y, gr.color_rgb(r//2, g, b))
    return img

def filter2(img):
    '''For x in range width and height is basically the rows and columns in other word its how u cover the whole image'''
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            (r, g, b) = img.getPixel(x, y)
            img.setPixel(x, y, gr.color_rgb(b, b, 0))
    return img

def filter3(img):
    '''For x in range width and height is basically the rows and columns in other word its how u cover the whole image'''
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            (r, g, b) = img.getPixel(x, y)
            img.setPixel(x, y, gr.color_rgb(g, r, 0))
    return img

def filter4(img):
    '''For x in range width and height is basically the rows and columns in other word its how u cover the whole image'''
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            (r, g, b) = img.getPixel(x, y)
            img.setPixel(x, y, gr.color_rgb(b, 0, r))
    return img

def test(filename):
    myImage = gr.Image(gr.Point(0, 0), filename)
    filter1image = gr.Image(gr.Point(0, 0), filename)
    filter2image = gr.Image(gr.Point(0, 0), filename)
    filter3image = gr.Image(gr.Point(0, 0), filename)
    filter4image = gr.Image(gr.Point(0, 0), filename)
   

    '''This basically appends the filter1 function into the filter1image variable created in the test function'''
    filter1(filter1image)
    '''Saves the image created and creates a file name for it within lab06 folder'''
    filter1image.save('filter1.ppm')

    '''This basically appends the filter2 function into the filter2image variable created in the test function'''
    filter2(filter2image)
    '''Saves the image created and creates a file name for it within lab06 folder'''
    filter2image.save('filter2.ppm')

    '''This basically appends the filter2 function into the filter2image variable created in the test function'''
    filter3(filter3image)
    '''Saves the image created and creates a file name for it within lab06 folder'''
    filter3image.save('filter3.ppm')

    '''This basically appends the filter2 function into the filter2image variable created in the test function'''
    filter4(filter4image)
    '''Saves the image created and creates a file name for it within lab06 folder'''
    filter4image.save('filter4.ppm')



#     '''This is just code to make sure the myImage variable is called... This is just so that it works'''
    myImage.save('flowersfilter.ppm')

# def greenScreen(greenImg, otherImg):
#     # screen = gr.GraphWin("my screen", 1000, 1000)
#     firstImg = gr.Image(gr.Point(0, 0), greenImg)
#     subImg = gr.Image(gr.Point(0, 0), otherImg)
#     # imageList = [firstImg, subImg]
#     # w = subImg.getWidth()
#     # h = subImg.getHeight()
#     w = firstImg.getWidth()
#     h = subImg.getHeight()
#     for x in range(w):
#         for y in range(h):
#             (r, g, b) = firstImg.getPixel(x, y)
#             (rr, gg, bb) = subImg.getPixel(x, y)
#             if (g > int(b * 1.5) and g > r):
#                 firstImg.setPixel(x, y, gr.color_rgb(rr, gg, bb))
#     return firstImg



'''Fran'''
def greenScreen(greenImg, otherImg):
    '''If a pixel in `greenImg` is very green, replace it with the corresponding pixel in `otherImg`.

A reasonable test for 'very green' is if the green pixel is 1.5 times the blue channel and also bigger than the red pixel.
Play around with the 1.5 number to see if you can get better results.
'''
    for x in range(greenImg.getWidth()):
        for y in range(greenImg.getHeight()):
            (r, g, b) = greenImg.getPixel(x, y)
            if g>1.5*b and g>r:
                (newR, newG, newB) = otherImg.getPixel(x, y)
                greenImg.setPixel(x, y, gr.color_rgb(newR, newG, newB))
    return greenImg


  
if __name__ == '__main__':
    # greenScreen("myGreenScreen.ppm", "exotics.ppm")
    
    # main()
    test('flowers.ppm')



# def filter1(Img):
#     '''Swaps the green and blue values of every pixel of a Zelle image `img`'''
#     for x in range(Img.getWidth()):
#         for y in range(Img.getHeight()):
#             (r, g, b) = Img.getPixel(x, y)
#             Img.setPixel(x,y ,gr.color_rgb(r//2, b, g))