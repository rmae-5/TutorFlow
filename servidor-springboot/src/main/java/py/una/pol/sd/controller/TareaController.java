package py.una.pol.sd.controller;

import org.springframework.web.bind.annotation.*;
import py.una.pol.sd.model.Tarea;
import py.una.pol.sd.service.TareaService;
import java.util.List;
import java.util.Optional;
import org.springframework.http.ResponseEntity;

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

    @PostMapping
    public Tarea crearTarea(@RequestBody Tarea tarea) {
        return service.guardar(tarea);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Tarea> actualizarTarea(@PathVariable Long id, @RequestBody Tarea tarea) {
        Optional<Tarea> updatedTarea = service.actualizar(id, tarea);
        return updatedTarea.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarTarea(@PathVariable Long id) {
        service.eliminar(id);
        return ResponseEntity.noContent().build();
    }
}
