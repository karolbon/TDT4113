from Proglab2.TDT4113.Project_5.imager.imager2 import Imager
from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageOps


class Artist:

    def __init__(self, path1, path2, path3):
        '''Oppretter Image objekter av bildene som tas inn'''

        self.path1, self.path2, self.path3 = path1, path2, path3


        self.image_1 = Image.open(path1)
        self.image_2 = Image.open(path2)
        self.image_3 = Image.open(path3)

        self.image_wrap_1 = self.create_image_wrappers(self.image_1, path1)
        self.image_wrap_2 = self.create_image_wrappers(self.image_2, path2)
        self.image_wrap_3 = self.create_image_wrappers(self.image_3, path3)

        self.collage = None
        self.collage_wrap = None
        self.artwork = None

    def create_image_wrappers(self, image, path):
        w, h = image.size

        img_wrap = Imager(path, image, w, h, background='black', mode='RGB')
        return img_wrap

    @staticmethod
    def img_width(img):
        return img.size[0]

    @staticmethod
    def img_height(img):
        return img.size[1]

    def create_collage(self):
        '''Lage en horisontal-kollasj av de tre bildene'''

        width = min(self.img_width(self.image_1), self.img_width(self.image_2), self.img_width(self.image_3))
        height = min(self.img_height(self.image_1), self.img_height(self.image_2), self.img_height(self.image_3))

        collage = Image.new('RGB', (width, height))

        img_width = width//3
        img_height = height

        im1 = self.image_1.resize((img_width, img_height))
        im2 = self.image_2.resize((img_width, img_height))
        im3 = self.image_3.resize((img_width, img_height))

        collage.paste(im1, (0, 0))
        collage.paste(im2, (int(width/3) , 0))
        collage.paste(im3, (int(2*width/3), 0))

        collage.save('collage.jpg')

        self.collage = Image.open('collage.jpg')
        self.collage_wrap = self.create_image_wrappers(self.collage, 'collage.jpg')

        return collage

    def draw_circle(self):
        w = self.img_width(self.collage)
        h = self.img_height(self.collage)
        draw = ImageDraw.Draw(self.collage)
        draw.ellipse((100, 100, 180, 180), fill=None, outline='black')
        self.collage.save('draw.png')
        self.draw = Image.open('draw.png')
        self.draw_wrapper = self.create_image_wrappers(self.draw, 'draw.png')
        return self.draw

    def gray_scale(self):
        gray = self.image_1.convert('1')
        gray.save('gray.png')
        self.image_1 = Image.open('gray.png')
        self.image_wrap_1 = self.create_image_wrappers(self.image_1, 'gray.png')
        return self.image_1

    def morph_pictures(self):
        '''Morph av bilde 2 og bilde 3'''

        self.image_wrap_2 = self.create_image_wrappers(self.image_2, self.path2)

        self.image_wrap_3 = self.create_image_wrappers(self.image_3, self.path3)

        mor = self.image_wrap_2.morph(self.image_wrap_3, alpha=0.75)

        mor.image.save('morph.png')

        self.image_2 = Image.open('morph.png')
        self.image_wrap_2 = self.create_image_wrappers(self.image_2, 'morph.png')
        self.image_wrap_3 = self.create_image_wrappers(self.image_3, self.path3)
        return mor

    def enhance_image(self):

        img_type = (self.path3.split('.'))

        if img_type[1] != "jpeg":
            self.path3 = img_type[0]+'.jpeg'
            self.image_3 = Image.open(self.path3)
            self.image_wrap_3 = self.create_image_wrappers(self.image_3, self.path3)

        bright_enhance = ImageEnhance.Brightness(self.image_3)
        img = bright_enhance.enhance(0.6)

        self.image_3 = img

    def mirror(self):
        self.collage = ImageOps.mirror(self.collage)

    def create_art(self):
        '''Bilde 1'''
        self.gray_scale()

        '''Bilde 2'''
        self.morph_pictures()

        '''Bilde 3'''
        self.enhance_image()

        '''Kollasj'''
        self.create_collage()

        '''Draw'''
        self.draw_circle()

        '''Mirror'''
        self.mirror()

    def show_art(self):
        self.artwork = self.collage
        self.artwork.show()




def main():
    artist = Artist('imager/images/donaldduck.jpeg', 'imager/images/minions.jpeg', 'imager/images/trail.gif')
    artist.create_art()
    artist.show_art()



main()