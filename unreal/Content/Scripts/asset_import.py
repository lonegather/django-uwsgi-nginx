import unreal_engine as ue


def import_asset(stage, source, target, skeleton=None):

    from unreal_engine.classes import PyFbxFactory, Skeleton
    from unreal_engine.enums import EFBXImportType

    target = target[:-1] if target[-1] in ['\\', '/'] else target

    ue.log('<<<--- stage: %s --->>>' % stage)
    ue.log('<<<--- source: %s --->>>' % source)
    ue.log('<<<--- target: %s --->>>' % target)
    ue.log('<<<--- skeleton: %s --->>>' % skeleton)

    factory = PyFbxFactory()
    factory.ImportUI.bCreatePhysicsAsset = False
    factory.ImportUI.bImportMaterials = True if stage in ['mdl'] else False
    factory.ImportUI.bImportAnimations = True if stage in ['cam', 'lyt', 'anm'] else False

    if stage == 'cam':
        setup_sequencer(source, target)
        return

    if stage in ['lyt', 'anm']:
        factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
        data = factory.ImportUI.AnimSequenceImportData
        data.CustomSampleRate = 25

        if not skeleton:
            ue.log_error("<<<--- No skeleton information found --->>>")
            return

        skel_assets = ue.get_assets_by_class('Skeleton')
        for skel in skel_assets:
            if skel.get_name().count(skeleton):
                ue.log('<<<--- Found skeleton "%s" --->>>' % skel.get_name())
                factory.ImportUI.skeleton = skel
                break
        else:
            ue.log_error('<<<--- No matching skeleton found for "%s" --->>>' % skeleton)
            return

    factory.factory_import_object(source, target)


def setup_sequencer(source, target):
    import os
    from unreal_engine.classes import LevelSequenceFactoryNew

    name = os.path.basename(source).lower().split('.fbx')[0]

    for seq in ue.get_assets_by_class('LevelSequence'):
        if seq.get_display_name() == name:
            break
    else:
        factory = LevelSequenceFactoryNew()
        seq = factory.factory_create_new(target + ('/%s' % name))

    print(seq.get_display_name())
