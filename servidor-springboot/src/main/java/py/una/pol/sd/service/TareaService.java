package py.una.pol.sd.service;

import org.springframework.stereotype.Service;
import py.una.pol.sd.model.Tarea;
import py.una.pol.sd.repository.TareaRepository;
import java.util.List;
import java.util.Optional;

@Service
public class TareaService {
    private final TareaRepository repo;

    public TareaService(TareaRepository repo) {
        this.repo = repo;
    }

    public List<Tarea> listarTodas() {
        return repo.findAll();
    }

    public Optional<Tarea> porId(Long idTarea) {
        return repo.findById(idTarea);
    }
}
