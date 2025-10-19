"""
BALLS
__main__.py
"""
import modules.window as window
import modules.colors as colors

def main() -> None:
    print("# Balls")    
    window.main(
        color_mode=colors.Mode.GRADIENT
    )

if __name__ == "__main__":
    main()
    

