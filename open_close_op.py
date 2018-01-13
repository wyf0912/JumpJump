import cv2


def open_op(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    opened_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return opened_mask


def open_op_large(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(8, 8))
    opened_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return opened_mask


def open_op_mid(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    opened_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return opened_mask


def close_op(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return closed_mask


def dila_op(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 6))
    closed_mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
    return closed_mask


def close_op_large(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(6, 12))
    closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return closed_mask