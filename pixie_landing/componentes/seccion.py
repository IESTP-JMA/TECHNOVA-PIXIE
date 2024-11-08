import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.hstack(
        rx.vstack(
          rx.heading(
            rx.text.span("PIXIE",color=rx.color("blue",7)),
            " la Aplicacion que te guia al tomarte una foto"
          ),
          rx.text("Mejora tus fotos con nuevas ideas",
          rx.text.em(" creativas,",color=rx.color("cyan",9)),
          "se la envidia de los demas con ",
          rx.text.quote("PIXIE.",color=rx.color("gold",9))),  
        ),
        rx.image(src="https://images.unsplash.com/photo-1543918965-abd9e8f100cb?q=80&w=1436&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",width="500px"),
      ),
      rx.link(
          rx.button(rx.icon(tag="airplay"),"Registrate",),
          href="https://forms.gle/PvYHtu3D2NfWUq3f6",
          is_external=True,
      ),
      align="center",
      text_align="center",
    )