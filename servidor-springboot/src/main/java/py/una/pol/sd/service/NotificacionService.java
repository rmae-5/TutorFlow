package py.una.pol.sd.service;

import org.springframework.stereotype.Service;
import py.una.pol.sd.model.Notificacion;
import py.una.pol.sd.repository.NotificacionRepository;
import java.util.List;
import java.util.Optional;

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

    public Notificacion guardar(Notificacion notificacion) {
        return repo.save(notificacion);
    }

    public Optional<Notificacion> actualizar(Long id, Notificacion notificacionActualizada) {
        return repo.findById(id).map(notificacion -> {
            notificacion.setIdUsuario(notificacionActualizada.getIdUsuario());
            notificacion.setMensaje(notificacionActualizada.getMensaje());
            notificacion.setFecha(notificacionActualizada.getFecha());
            return repo.save(notificacion);
        });
    }

    public void eliminar(Long id) {
        repo.deleteById(id);
    }
}
