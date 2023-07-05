def solution(picture, k):
    zoom_in = []
    for pixel in picture:
        new_pixel = ''
        for p in pixel:
            new_pixel += p*k
        zoom_in.append(new_pixel)
    return [s for s in zoom_in for _ in range(k)]