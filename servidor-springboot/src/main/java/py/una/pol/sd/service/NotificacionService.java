package py.una.pol.sd.service;

import org.springframework.stereotype.Service;
import py.una.pol.sd.model.Notificacion;
import py.una.pol.sd.repository.NotificacionRepository;
import java.util.List;

@Service
public class NotificacionService {
    private final NotificacionRepository repo;

    public NotificacionService(NotificacionRepository repo) {
        this.repo = repo;
    }

    public List<Notificacion> listarTodas() {
        return repo.findAll();
    }

    public List<Notificacion> porUsuario(Long idUsuario) {
        return repo.findByIdUsuario(idUsuario);
    }
}
