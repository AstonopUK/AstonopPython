import ctypes
import ctypes.wintypes

def displayGammaValues(lpRamp):
    """
    Displays the GammaArray of 256 values of R,G,B individually
    :param lpRamp: GammaArray
    :return: None
    """
    print("R values: ", end=' ')
    for j in range(256):
        print(lpRamp[0][j], end=' ')
    print()

    print("G values: ", end=' ')
    for j in range(256):
        print(lpRamp[0][j], end=' ')
    print()

    print("B values: ", end=' ')
    for j in range(256):
        print(lpRamp[0][j], end=' ')
    print(), print()


def changeGammaValues(lpRamp, brightness):
    """
    Modifies the Gamma Values array according to specified 'Brightness' value
    To reset the gamma values to default, call this method with 'Brightness' as 128
    :param lpRamp: GammaArray
    :param brightness: Value of brightness between 0-255
    :return: Modified GammaValue Array
    """
    for i in range(256):
        iValue = i * (brightness + 128)
        if iValue > 65535: iValue = 65535
        lpRamp[0][i] = lpRamp[1][i] = lpRamp[2][i] = iValue
    return lpRamp


if __name__ == '__main__':    # can be aby value in 0-255 (as per my system)
    GetDC = ctypes.windll.user32.GetDC
    ReleaseDC = ctypes.windll.user32.ReleaseDC
    SetDeviceGammaRamp = ctypes.windll.gdi32.SetDeviceGammaRamp
    GetDeviceGammaRamp = ctypes.windll.gdi32.GetDeviceGammaRamp

    hdc = ctypes.wintypes.HDC(GetDC(None))
    if hdc:
        GammaArray = ((ctypes.wintypes.WORD * 256) * 3)()
        if GetDeviceGammaRamp(hdc, ctypes.byref(GammaArray)):
            for x in range(100):
                brightness = 1
                GammaArray = changeGammaValues(GammaArray, brightness)

                if SetDeviceGammaRamp(hdc, ctypes.byref(GammaArray)): pass
                else: print("Unable to set GammaRamp")
                
                brightness = 255
                GammaArray = changeGammaValues(GammaArray, brightness)

                if SetDeviceGammaRamp(hdc, ctypes.byref(GammaArray)): pass
                else: print("Unable to set GammaRamp")
                    
            brightness = 125
            GammaArray = changeGammaValues(GammaArray, brightness)            
            if SetDeviceGammaRamp(hdc, ctypes.byref(GammaArray)): pass
        else: print("Unable to set GammaRamp")
        if ReleaseDC(hdc): print("HDC released")
    else: print("HDC not found")
