#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {
}

moscow_london_dist = ((sites['Moscow'][0]-sites['London'][0])**2 + (sites['Moscow'][1]-sites['London'][1])**2)**0.5
moscow_paris_dist = ((sites['Moscow'][0]-sites['Paris'][0])**2 + (sites['Moscow'][1]-sites['Paris'][1])**2)**0.5
london_paris_dist = ((sites['London'][0]-sites['Paris'][0])**2 + (sites['London'][1]-sites['Paris'][1])**2)**0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london_dist
distances['Moscow']['Paris'] = moscow_paris_dist

distances['London'] = {}
distances['London']['Moscow'] = moscow_london_dist
distances['London']['Paris'] = london_paris_dist

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_paris_dist
distances['Paris']['London'] = london_paris_dist

print(distances)




