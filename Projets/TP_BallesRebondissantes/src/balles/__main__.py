"""
BALLS
__main__.py
"""
import modules.window as window
import modules.colors as colors

def main() -> None:
    print("# Balls")    
    
    color_mode = colors.Mode.GRADIENT
    print(f"Color mode: {color_mode}")
    
    window.main(
        color_mode=color_mode,
    )

if __name__ == "__main__":
    main()
    

