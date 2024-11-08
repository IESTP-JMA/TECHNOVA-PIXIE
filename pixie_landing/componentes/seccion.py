import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("PIXIE",color=rx.color("blue",7)),
        " la Aplicacion que te guia al tomarte una foto"),

      rx.container(
        rx.text("Mejora tus fotos con nuevas ideas",
        rx.text.em(" creativas,",color=rx.color("cyan",9)),
        "se la envidia de los demas con ",
        rx.text.quote("PIXIE.",color=rx.color("gold",9))),
        rx.link(
          rx.button(rx.icon(tag="airplay"),"Registrate",),
          href="https://forms.gle/PvYHtu3D2NfWUq3f6",
          is_external=True,
          margin_top="3em",
        ),
      ),
      padding_top="8em",
      align="center",
      text_align="center",
      height="800px"
    )