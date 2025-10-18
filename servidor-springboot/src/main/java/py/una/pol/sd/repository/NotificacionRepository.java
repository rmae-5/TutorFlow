package py.una.pol.sd.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import py.una.pol.sd.model.Notificacion;
import java.util.List;

public interface NotificacionRepository extends JpaRepository<Notificacion, Long> {
    List<Notificacion> findByIdUsuario(Long idUsuario);
}
