package py.una.pol.sd.controller;

import org.springframework.web.bind.annotation.*;
import py.una.pol.sd.model.Tarea;
import py.una.pol.sd.service.TareaService;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/tareas")
public class TareaController {

    private final TareaService service;

    public TareaController(TareaService service) {
        this.service = service;
    }

    @GetMapping
    public List<Tarea> listarTodas() {
        return service.listarTodas();
    }

    @GetMapping("/{idTarea}")
    public Optional<Tarea> porId(@PathVariable Long idTarea) {
        return service.porId(idTarea);
    }
}
