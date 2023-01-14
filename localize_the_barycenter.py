def bar_triang(point_a, point_b, point_c): 
    barycenter_x = round((point_a[0] + point_b[0] + point_c[0])/3, 4)
    barycenter_y = round((point_a[1] + point_b[1] + point_c[1])/3, 4)
    return [barycenter_x, barycenter_y]
