# style.py

button_nav_style = dict(
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="white",
    opacity="0.8",
    _hover={
        "opacity": 2,
    },
)

style = {
    ".card-container"  :  {
        "opacity": "1", #/* La tarjeta estará inicialmente oculta */
        "transform": "translateY(10px)", #/* La tarjeta estará ligeramente desplazada hacia abajo */
        "transition": "opacity 0.5s ease, transform 0.5s ease"
    },

   ".card"  :  {  
        "border-radius": "10px",
        "box-shadow":" 0px 2px 10px rgba(0, 0, 0, 0.2)",
        "opacity": "1", #/* La tarjeta estará inicialmente oculta */
        "transform": "translateY(10px)", #/* La tarjeta estará ligeramente desplazada hacia abajo */
        "transition": "opacity 0.5s ease, transform 0.5s ease"  
   }
}