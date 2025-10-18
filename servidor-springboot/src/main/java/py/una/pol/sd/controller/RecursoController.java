package py.una.pol.sd.controller;

import org.springframework.web.bind.annotation.*;
import py.una.pol.sd.model.Recurso;
import py.una.pol.sd.service.RecursoService;
import java.util.List;
import java.util.Optional;
import org.springframework.http.ResponseEntity;

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

    @PostMapping
    public Recurso crearRecurso(@RequestBody Recurso recurso) {
        return service.guardar(recurso);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Recurso> actualizarRecurso(@PathVariable Long id, @RequestBody Recurso recurso) {
        Optional<Recurso> updatedRecurso = service.actualizar(id, recurso);
        return updatedRecurso.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarRecurso(@PathVariable Long id) {
        service.eliminar(id);
        return ResponseEntity.noContent().build();
    }
}
