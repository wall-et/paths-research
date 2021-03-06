from view import View
from model import Model
import re

import pandas as pd

from settings import DEFUALT_IMAGE_FILE, DEFUALT_DATA_FILE,GENERAL_SETTINGS


class Controller:
    def __init__(self):
        self.config = GENERAL_SETTINGS

        self.m = Model()
        # self.m.config = self.config
        self.v = View()
        # self.v.config = self.config
        self.file = self.v.get_file()
        self.file = self.file if self.file else DEFUALT_DATA_FILE
        self.image = self.v.get_image()
        self.image = self.image if self.image else DEFUALT_IMAGE_FILE
        self.filters = dict({'area': None, 'hour': None, 'date': None, 'block': None})

    def fix_data(self):
        self.m.fix_corrupted_file(self.file)
        self.m.load_data(self.file)

    def initial_run(self):
        self.v.set_image(self.image)
        self.m.load_data(self.file)
        self.v.plot_image_and_routes(self.m.get_data(self.filters))

    # def shift_cmd(self):
    #     print(self.filters)
    #     x1 , y1 ,x2,y2 = input("update vals")
    #     if self.filters['area'] = {x1:{}}
    #
    #

    def run(self):
        self.initial_run()
        self.v.output("Displaying the first 100 rounds.\navailable: filter,grid,config,exit")
        cmd = "init"
        while cmd != 'exit':
            # self.shift_cmd()
            if self.string_found("filter",cmd):
                self.filters = self.v.get_filters(self.filters)
                self.v.plot_image_and_routes(self.m.get_data(self.filters))
            if self.string_found("grid", cmd):
                self.v.draw_grid()
            if self.string_found("config", cmd):
                n_conf = self.v.set_config(self.config)
                self.set_filters(n_conf)
            self.v.output("Enter Command:")
            cmd = self.v.get_input()

            # if self.string_found("block", cmd) or self.string_found("f4", cmd):
            #     list_block = [int(x) for x in cmd.split()[1:]]
            #     img = plt.imread(self.image)
            #     print(img.shape)
            #     self.v.plot_image_and_routes(self.m.data, self.m.get_square_routes(list_block, img.shape))


    def string_found(self, string1, string2):
        if re.search(r"\b" + re.escape(string1) + r"\b", string2):
            return True
        return False

    def set_filters(self,n_conf):
        # if self.config['num_of_blocks_in_image'] != n_conf['num_of_blocks_in_image']:
        #     self.config['num_of_blocks_in_image'] = n_conf['num_of_blocks_in_image']
        #     self.m.NUM_SLICE_X = self.config['num_of_blocks_in_image']
        #     self.m.NUM_SLICE_Y = self.config['num_of_blocks_in_image']
        # if self.config['auto_load_path_by_path'] != n_conf['auto_load_path_by_path']:
        #     self.config['auto_load_path_by_path'] = n_conf['auto_load_path_by_path']
        # if self.config['hard_reload_data_files'] != n_conf['hard_reload_data_files']:
        #     self.config['hard_reload_data_files'] = n_conf['hard_reload_data_files']
        self.config = n_conf
        self.m.config = self.config
        self.v.config = self.config
        self.v.NUM_SLICE = self.config['num_of_blocks_in_image']
        self.m.NUM_SLICE_X = self.config['num_of_blocks_in_image']
        self.m.NUM_SLICE_Y = self.config['num_of_blocks_in_image']