package py.una.pol.sd.controller;

import org.springframework.web.bind.annotation.*;
import py.una.pol.sd.model.Notificacion;
import py.una.pol.sd.service.NotificacionService;
import java.util.List;

@RestController
@RequestMapping("/notificaciones")
public class NotificacionController {

    private final NotificacionService service;

    public NotificacionController(NotificacionService service) {
        this.service = service;
    }

    @GetMapping
    public List<Notificacion> listarTodas() {
        return service.listarTodas();
    }

    @GetMapping("/{idUsuario}")
    public List<Notificacion> porUsuario(@PathVariable Long idUsuario) {
        return service.porUsuario(idUsuario);
    }
}
