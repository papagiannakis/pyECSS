.. _TutorialEntity:
Create an entity
==================

In this tutorial we will demonstrate how to create and use an entity.

This code creates an Object entity and adds it to the scene

.. code-block:: python

    object1 = scene.world.createEntity(Entity("Object"));
    scene.world.addEntityChild(scene.world.root, object1);

The implementation is simple but remember to attach your component to the scene graph after generating it.

This second code snippet creates an entity and adds it to the scene in one single line.

.. code-block:: python

    myObject = scene.world.createEntity(Entity("Object"));


.. note:: 
    
    Entities are initialized as empty objects. Later you will attach components and apply functionality to them.
