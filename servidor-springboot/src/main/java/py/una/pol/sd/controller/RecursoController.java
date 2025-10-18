package py.una.pol.sd.controller;

import org.springframework.web.bind.annotation.*;
import py.una.pol.sd.model.Recurso;
import py.una.pol.sd.service.RecursoService;
import java.util.List;

@RestController
@RequestMapping("/recursos")
public class RecursoController {

    private final RecursoService service;

    public RecursoController(RecursoService service) {
        this.service = service;
    }

    @GetMapping
    public List<Recurso> listarTodos(@RequestParam(required = false) String materia) {
        if (materia != null) {
            return service.porMateria(materia);
        }
        return service.listarTodos();
    }
}
