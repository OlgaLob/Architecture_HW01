package InMemoryModel;

import java.util.ArrayList;
import java.util.List;

import ModelElemrnts.Camera;
import ModelElemrnts.Flash;
import ModelElemrnts.PoligonalModel;
import ModelElemrnts.Scene;

public class ModelStore {
    public List<PoligonalModel> Models;
    public List<Scene> Scenes;
    public List<Flash> Flashes;
    public List<Camera> Cameras;
    private List<IModelChangeObserver> ChangeObservers;

    /**
     * конструктор
     *
     * @param texture
     * @throws Exception
     */
    public ModelStore(List<IModelChangeObserver> changeObservers) throws Exception {
        this.ChangeObservers = changeObservers;

        this.Models = new ArrayList<>();
        this.Scenes = new ArrayList<>();
        this.Flashes = new ArrayList<>();
        this.Cameras = new ArrayList<>();

        Models.add(new PoligonalModel(null));
        Flashes.add(new Flash());
        Cameras.add(new Camera());
        Scenes.add(new Scene(0,Models,Flashes, Cameras));
    }


   
    public Scene GetScena(int ID) {
        for (int i = 0; i < Scenes.size(); i++) {
            if (Scenes.get(i).ID == ID) {
                return Scenes.get(i);
            }

        }
        return null;
    }

    
    public void NotifyChange(IModelChanger sender) {

    }
}
