# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            # Handle special items that increase in quality
            if not item.name.startswith("Aged Brie") and not item.name.startswith("Backstage passes"):
                if item.quality > 0:
                    if not item.name.startswith("Sulfuras"):
                        #Added conjured items
                        if item.name.startswith("Conjured"):
                            # As quality cannot go below zero
                            item.quality = max(0, item.quality - 2)
                        else:
                            item.quality = max(0, item.quality - 1)
            else:
                # Aged Brie and Backstage passes increase in quality
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name.startswith("Backstage passes"):
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            
            # Decrease sell_in for all items except Sulfuras
            if not item.name.startswith("Sulfuras"):
                item.sell_in = item.sell_in - 1
            
            # Handle post-expiration effects
            if item.sell_in < 0:
                if not item.name.startswith("Aged Brie"):
                    if not item.name.startswith("Backstage passes"):
                        if item.quality > 0:
                            if not item.name.startswith("Sulfuras"):
                                # code to handle conjured items after degradation
                                if item.name.startswith("Conjured"):
                                    # As quality cannot go below zero
                                    item.quality = max(0, item.quality - 2)
                                else:
                                    item.quality = max(0, item.quality - 1)
                    else:
                        # Backstage passes become worthless after concert
                        item.quality = item.quality - item.quality
                else:
                    # Aged Brie continues to improve even after expiration
                    if item.quality < 50:
                        item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
