import math
import vtk
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QAction, QErrorMessage, QHBoxLayout, QInputDialog,
                             QLabel)
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

actor = vtk.vtkActor()
shapes = [actor]
shapeNameslist = ["Item 1"]
index = -1


class MyRenderWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_actor = None

        # Create a button to draw the line
        self.draw_button = QtWidgets.QPushButton("Draw Line")
        self.draw_button.clicked.connect(self.draw_line)

        # Create a button to draw a polyline
        self.draw_polyline_button = QtWidgets.QPushButton("Draw Polyline")
        self.draw_polyline_button.clicked.connect(self.draw_polyline)

        # Create a button to draw a polygon
        self.draw_polygon_button = QtWidgets.QPushButton("Draw polygon")
        self.draw_polygon_button.clicked.connect(self.draw_polygon)

        # Create a button to draw a Irregular polygon
        self.draw_irr_polygon_button = QtWidgets.QPushButton(
            "Draw Irregular polygon")
        self.draw_irr_polygon_button.clicked.connect(self.draw_irr_polygon)

        # Create a button to draw a circle
        self.draw_circle_button = QtWidgets.QPushButton("Draw circle")
        self.draw_circle_button.clicked.connect(self.draw_circle)

        # Create a button to draw an arc
        self.draw_arc_button = QtWidgets.QPushButton("Draw arc")
        self.draw_arc_button.clicked.connect(self.draw_arc)

        # Create a button to draw an Ellipse
        self.draw_ellipse_button = QtWidgets.QPushButton("Draw Ellipse")
        self.draw_ellipse_button.clicked.connect(self.draw_ellipse)

        self.draw_sphere_button = QtWidgets.QPushButton("Draw 3D Sphere")
        self.draw_sphere_button.clicked.connect(self.draw_sphere)

        self.draw_ellipsoid_button = QtWidgets.QPushButton("Draw 3D Ellipsoid")
        self.draw_ellipsoid_button.clicked.connect(self.draw_ellipsoid)

        self.draw_cube_button = QtWidgets.QPushButton("Draw 3D Cube")
        self.draw_cube_button.clicked.connect(self.draw_cube)

        # Create a color button to change the line color
        self.color_button = QtWidgets.QPushButton("Change Color")
        self.color_button.clicked.connect(self.change_color)

        self.scalingButton = QtWidgets.QPushButton("Scale")
        self.scalingButton.clicked.connect(self.onScaleClicked)

        self.delete_button = QtWidgets.QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.delete_object)

        # Create a button to exit the application
        self.exit_button = QtWidgets.QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)

        # Create labels to display mouse position
        self.x_label = QLabel(self)
        self.y_label = QLabel(self)

        # Create a VTK render window and renderer
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)

        # Set the background color of the renderer
        self.renderer.SetBackground(0.8, 0.8, 0.8)

        # Set up a vtkInteractorStyle to handle user input
        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(
            vtk.vtkInteractorStyleTrackballCamera())

        self.combo_box = QtWidgets.QComboBox(self)

        # Set up the main window layout with the draw and exit buttons and mouse position labels
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.draw_button)
        button_layout.addWidget(self.draw_polyline_button)
        button_layout.addWidget(self.draw_polygon_button)
        button_layout.addWidget(self.draw_irr_polygon_button)
        button_layout.addWidget(self.draw_circle_button)
        button_layout.addWidget(self.draw_arc_button)
        button_layout.addWidget(self.draw_ellipse_button)
        button_layout.addWidget(self.draw_sphere_button)
        button_layout.addWidget(self.draw_ellipsoid_button)
        button_layout.addWidget(self.draw_cube_button)
        dropdown_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(self.scalingButton)

        button_layout.addWidget(self.color_button)
        button_layout.addWidget(self.exit_button)
        label_layout = QtWidgets.QHBoxLayout()
        label_layout.addWidget(QLabel("X:"))
        label_layout.addWidget(self.x_label)
        label_layout.addWidget(QLabel("Y:"))
        label_layout.addWidget(self.y_label)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.vtk_widget)
        layout.addLayout(button_layout)
        layout.addLayout(label_layout)
        layout.addLayout(dropdown_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a menu bar with a "Clear All" action
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        clear_all_action = QAction("Clear All", self)
        clear_all_action.triggered.connect(self.clear_all)
        file_menu.addAction(clear_all_action)
        # Create a "Save" action to save the line coordinates to a file
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        # Create a "load" action to load the line coordinates to a file
        load_action = QAction("Load", self)
        load_action.triggered.connect(self.load_file)
        file_menu.addAction(load_action)

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_object)
        file_menu.addAction(delete_action)

        menu_bar2 = self.menuBar()
        translate_menu = menu_bar2.addMenu("Translate")

        line_action = QAction("Line", self)
        line_action.triggered.connect(self.Translate_line)
        translate_menu.addAction(line_action)

        polyline_action = QAction("Polyline", self)
        polyline_action.triggered.connect(self.Translate_polyline)
        translate_menu.addAction(polyline_action)

        ellipse_action = QAction("Ellipse", self)
        ellipse_action.triggered.connect(self.Translate_ellipse)
        translate_menu.addAction(ellipse_action)

        polygon_action = QAction("Polygon", self)
        polygon_action.triggered.connect(self.Translate_polygon)
        translate_menu.addAction(polygon_action)

        irr_polygon_action = QAction("Irregular Polygon", self)
        irr_polygon_action.triggered.connect(self.Translate_irr_polygon)
        translate_menu.addAction(irr_polygon_action)

        arc_action = QAction("Arc", self)
        arc_action.triggered.connect(self.Translate_arc)
        translate_menu.addAction(arc_action)

        circle_action = QAction("Circle", self)
        circle_action.triggered.connect(self.Translate_Circle)
        translate_menu.addAction(circle_action)

        cube_action = QAction("Cube", self)
        cube_action.triggered.connect(self.Translate_Cube)
        translate_menu.addAction(cube_action)

        ellipsoid_action = QAction("Ellipsoid", self)
        ellipsoid_action.triggered.connect(self.Translate_Ellipsoid)
        translate_menu.addAction(ellipsoid_action)

        sphere_action = QAction("Sphere", self)
        sphere_action.triggered.connect(self.Translate_Sphere)
        translate_menu.addAction(sphere_action)

        menu_bar3 = self.menuBar()
        shearing_menu = menu_bar3.addMenu("Shearing")

        line_action = QAction("Line", self)
        line_action.triggered.connect(self.Shear_line)
        shearing_menu.addAction(line_action)

        ellipse_action = QAction("Ellipse", self)
        ellipse_action.triggered.connect(self.Shear_Ellipse)
        shearing_menu.addAction(ellipse_action)

        polygon_action = QAction("Polygon", self)
        polygon_action.triggered.connect(self.Shear_Polygon)
        shearing_menu.addAction(polygon_action)

        irr_polygon_action = QAction("Irregular Polygon", self)
        irr_polygon_action.triggered.connect(self.Shear_irr_polygon)
        shearing_menu.addAction(irr_polygon_action)

        arc_action = QAction("Arc", self)
        arc_action.triggered.connect(self.Shear_Arc)
        shearing_menu.addAction(arc_action)

        polyline_action = QAction("Polyline", self)
        polyline_action.triggered.connect(self.Shear_Polyline)
        shearing_menu.addAction(polyline_action)

        circle_action = QAction("Circle", self)
        circle_action.triggered.connect(self.Shear_Circle)
        shearing_menu.addAction(circle_action)

        cube_shear = QAction("Cube", self)
        cube_shear.triggered.connect(self.Shear_Cube)
        shearing_menu.addAction(cube_shear)

        sphere_Shear = QAction("Sphere", self)
        sphere_Shear.triggered.connect(self.Shear_Sphere)
        shearing_menu.addAction(sphere_Shear)

        ellipsoid_shear = QAction("Ellipsoid", self)
        ellipsoid_shear.triggered.connect(self.Shear_Ellipsoid)
        shearing_menu.addAction(ellipsoid_shear)

        # Set the title of the main window
        self.setWindowTitle("LineLegend")

        # Set the default line color to red
        self.line_color = (1, 0, 0)
        self.polyline_color = (1, 0, 0)
        self.polygon_color = (1, 0, 0)
        self.irr_polygon_color = (1, 0, 0)
        self.circle_color = (1, 0, 0)
        self.arc_color = (1, 0, 0)
        self.ellipse_color = (1, 0, 0)
        self.sphere_color = (1, 0, 0)
        self.ellipsoide_color = (1, 0, 0)
        self.cube_color = (1, 0, 0)

        # Show the window
        self.show()
        self.clear_all()
        self.showMaximized()

        # Set up mouse event handling
        self.interactor.AddObserver("MouseMoveEvent", self.mouse_move_event)

    def addItems(self, source, shapeName, index):
        self.dropdown.addItem(shapeName)
        shapes.append(source)

        shapeNameslist.append(shapeName)

        index += 1
        return shapes

    def selectShapes(self):
        selected_item = self.dropdown.currentText()

        position = -1
        for x in range(len(shapes)):
            position += 1
            if shapeNameslist[x] == selected_item:
                break
        print(shapeNameslist[position])
        return shapes[position]

    def delete_object(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        if current_actor:
            self.renderer.RemoveActor(current_actor)
            self.vtk_widget.GetRenderWindow().Render()

    def select_shape(self, x, y):
        # Create a picker and set its tolerance (in pixels)
        picker = vtk.vtkPropPicker()
        picker.SetTolerance(0.01)

        # Pick from the center of the screen
        picker.Pick(x, y, 0, self.renderer)

        # Get the picked actor
        actor = picker.GetActor()

        # If an actor was picked, do something
        if actor:
            # Set the selected actor as the current actor
            self.current_actor = actor

            # Highlight the selected actor with a different color
            self.current_actor.GetProperty().SetColor(self.highlight_color)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()

            # Update the shear and transform controls to show the selected shape's current values
            # (you will need to implement this yourself)
            self.update_shear_controls()
            self.update_transform_controls()

    def draw_polyline(self):
        # Ask the user for polyline coordinates
        coords, ok_pressed = QInputDialog.getText(
            self, "Enter polyline coordinates", "x1 y1 z1 x2 y2 z2 ... xn yn zn", QtWidgets.QLineEdit.Normal, "0 0 0 1 1 1")
        if not ok_pressed:
            return
        coords_list = coords.split(" ")
        if len(coords_list) % 3 != 0:
            error_dialog = QErrorMessage()
            error_dialog.showMessage("Invalid coordinates")
            return
        # Create a points array from the given coordinates
        points = vtk.vtkPoints()
        for i in range(0, len(coords_list), 3):
            points.InsertNextPoint(float(coords_list[i]), float(
                coords_list[i+1]), float(coords_list[i+2]))

        # Create a polyline from the points
        polyline = vtk.vtkPolyLine()
        polyline.GetPointIds().SetNumberOfIds(len(coords_list) // 3)
        for i in range(len(coords_list) // 3):
            polyline.GetPointIds().SetId(i, i)

        # Create a cell array and add the polyline to it
        cells = vtk.vtkCellArray()
        cells.InsertNextCell(polyline)

        # Create a polydata object and add the points and cells to it
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetLines(cells)

        # Create a mapper and actor to render the polyline
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the polyline
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the polyline actor in a class attribute
        self.polyline_actor = actor

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

        # Store the polyline coordinates in a class attribute
        self.polyline_coords = [float(coord) for coord in coords_list]

    def draw_line(self):
        # Ask the user for line coordinates
        coords, ok_pressed = QInputDialog.getText(
            self, "Enter line coordinates", "x1 y1 z1 x2 y2 z2", QtWidgets.QLineEdit.Normal, "0 0 0 1 1 1")
        if not ok_pressed:
            return
        coords_list = coords.split(" ")
        if len(coords_list) != 6:
            error_dialog = QErrorMessage()
            error_dialog.showMessage("Invalid coordinates")
            return

        # Create a line source with the given coordinates
        line = vtk.vtkLineSource()
        line.SetPoint1(float(coords_list[0]), float(
            coords_list[1]), float(coords_list[2]))
        line.SetPoint2(float(coords_list[3]), float(
            coords_list[4]), float(coords_list[5]))

        # Create a mapper and actor to render the line
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(line.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the line
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the line actor in a class attribute
        self.line_actor = actor

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

        # Store the line coordinates in a class attribute
        self.line_coords = [float(coord) for coord in coords_list]

    def change_color(self):
        # Open a color dialog to allow the user to select a new color
        color = QtWidgets.QColorDialog.getColor()

        # Set the color of the line actor to the selected color
        if color.isValid():
            r, g, b, _ = color.getRgbF()
            self.line_color = (r, g, b)
            if hasattr(self, 'line_actor'):
                self.line_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'polyline_actor'):
                self.polyline_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'polygon_actor'):
                self.polygon_actor.GetProperty().SetColor(self.line_color)
            # if hasattr(self, 'irr_polygon_actor'):
                # self.irr_polygon_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'circle_actor'):
                self.circle_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'arc_actor'):
                self.arc_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'ellipse_actor'):
                self.ellipse_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'sphere_actor'):
                self.sphere_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'ellipsoid_actor'):
                self.ellipsoid_actor.GetProperty().SetColor(self.line_color)
            if hasattr(self, 'cube_actor'):
                self.cube_actor.GetProperty().SetColor(self.line_color)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()

    def clear_all(self):
        # Remove all actors from the renderer
        self.renderer.RemoveAllViewProps()

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    def save_file(self):
        # Ask the user for a file name and location to save the line data
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Shape Data", "", "Text Files (*.txt)")

        # Save the line data to the file
        with open(file_path, "w") as f:
            if hasattr(self, "line_coords"):
                f.write("line\n")
                f.write(" ".join(str(coord)
                        for coord in self.line_coords) + "\n")
                f.write(" ".join(str(c) for c in self.line_color) + "\n")
            elif hasattr(self, "polygon_num_sides") and hasattr(self, "polygon_radius"):
                f.write("polygon\n")
                f.write(f"{self.polygon_num_sides} {self.polygon_radius}\n")
                f.write(" ".join(str(c) for c in self.line_color) + "\n")
            elif hasattr(self, "polyline_coords"):
                f.write("polyline\n")
                f.write(" ".join(str(coord)
                        for coord in self.polyline_coords) + "\n")
                f.write(" ".join(str(c) for c in self.line_color) + "\n")
            elif hasattr(self, "circle_actor"):
                circle_center = self.circle_actor.GetCenter()
                circle_points = self.circle_actor.GetMapper().GetInput().GetPoints()
                circle_point = [circle_points.GetPoint(i) for i in range(
                    circle_points.GetNumberOfPoints())][0]
                circle_radius = ((circle_point[0] - circle_center[0]) ** 2 + (
                    circle_point[1] - circle_center[1]) ** 2 + (circle_point[2] - circle_center[2]) ** 2) ** 0.5
                circle_color = self.circle_actor.GetProperty().GetColor()
                f.write("circle\n")
                f.write(
                    f"{self.circle_actor.GetCenter()[0]} {self.circle_actor.GetCenter()[1]} {self.circle_actor.GetCenter()[2]}\n")
                f.write(
                    f"{circle_radius}\n")
                f.write(
                    f"{circle_color[0]} {circle_color[1]} {circle_color[2]}\n")
            elif hasattr(self, "arc_actor"):
                arc_center = self.arc_params["center"]
                arc_radius = self.arc_params["radius"]
                arc_start_angle = self.arc_params["start_angle"]
                arc_end_angle = self.arc_params["end_angle"]
                arc_color = self.arc_actor.GetProperty().GetColor()
                arc_points = self.arc_actor.GetMapper().GetInput().GetPoints()
                arc_points = [arc_points.GetPoint(i) for i in range(
                    arc_points.GetNumberOfPoints())]
                arc_points = [tuple(point) for point in arc_points]
                f.write("arc\n")
                f.write(f"{arc_center[0]} {arc_center[1]} {arc_center[2]}\n")
                f.write(f"{arc_radius}\n")
                f.write(f"{arc_start_angle}\n")
                f.write(f"{arc_end_angle}\n")
                f.write(f"{arc_color[0]} {arc_color[1]} {arc_color[2]}\n")
                # Number of points used to approximate the arc
                f.write(f"{self.arc_params['n']}\n")
            elif hasattr(self, "ellipse_actor"):
                ellipse_center = self.ellipse_params["center"]
                ellipse_a = self.ellipse_params["a"]
                ellipse_b = self.ellipse_params["b"]
                ellipse_color = self.ellipse_actor.GetProperty().GetColor()

                # Get the ellipse points and convert them to a list of tuples
                ellipse_points = self.ellipse_actor.GetMapper().GetInput().GetPoints()
                ellipse_points = [ellipse_points.GetPoint(
                    i) for i in range(ellipse_points.GetNumberOfPoints())]
                ellipse_points = [tuple(point) for point in ellipse_points]

                f.write("ellipse\n")
                f.write(
                    f"{ellipse_center[0]} {ellipse_center[1]} {ellipse_center[2]} {ellipse_a} {ellipse_b}\n")
                f.write(
                    f"{ellipse_color[0]} {ellipse_color[1]} {ellipse_color[2]}\n")
                # Number of points used to approximate the ellipse
                f.write(f"{self.ellipse_params['n']}\n")
                for point in ellipse_points:
                    f.write(f"{point[0]} {point[1]} {point[2]}\n")
            elif hasattr(self, "sphere_actor"):
                sphere_center = self.sphere_center
                sphere_radius = self.sphere_radius
                sphere_resolution = self.sphere_resolution
                sphere_color = self.sphere_actor.GetProperty().GetColor()

                f.write("sphere\n")
                f.write(
                    f"{sphere_center[0]} {sphere_center[1]} {sphere_center[2]} {sphere_radius} {sphere_resolution}\n")
                f.write(
                    f"{sphere_color[0]} {sphere_color[1]} {sphere_color[2]}\n")
            elif hasattr(self, "ellipsoid_actor"):
                ellipsoid_center = self.ellipsoid_params["center"]
                ellipsoid_a = self.ellipsoid_params["a"]
                ellipsoid_b = self.ellipsoid_params["b"]
                ellipsoid_c = self.ellipsoid_params["c"]
                ellipsoid_color = self.ellipsoid_actor.GetProperty().GetColor()

                # Get the ellipsoid points and convert them to a list of tuples
                ellipsoid_points = self.ellipsoid_actor.GetMapper().GetInput().GetPoints()
                ellipsoid_points = [ellipsoid_points.GetPoint(
                    i) for i in range(ellipsoid_points.GetNumberOfPoints())]
                ellipsoid_points = [tuple(point) for point in ellipsoid_points]

                f.write("ellipsoid\n")
                f.write(
                    f"{ellipsoid_center[0]} {ellipsoid_center[1]} {ellipsoid_center[2]} {ellipsoid_a} {ellipsoid_b} {ellipsoid_c}\n")
                f.write(
                    f"{ellipsoid_color[0]} {ellipsoid_color[1]} {ellipsoid_color[2]}\n")
                # Number of points used to approximate the ellipsoid
                f.write(f"{len(ellipsoid_points)}\n")
                for point in ellipsoid_points:
                    f.write(f"{point[0]} {point[1]} {point[2]}\n")
            elif hasattr(self, "cube_actor"):
                cube_center = self.cube_center
                cube_size = self.cube_size
                cube_color = self.cube_actor.GetProperty().GetColor()

                f.write("cube\n")
                f.write(
                    f"{cube_center[0]} {cube_center[1]} {cube_center[2]} {cube_size}\n")
                f.write(f"{cube_color[0]} {cube_color[1]} {cube_color[2]}\n")

    def load_file(self):
        # Ask the user for a file to load line data from
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Load Line Data", "", "Text Files (*.txt)")

        # Load the data from the file
        with open(file_path, "r") as f:
            data = f.readlines()
            if len(data) < 2:
                error_dialog = QErrorMessage()
                error_dialog.showMessage("Invalid file format")
            object_type = data[0].strip()
            if object_type == "line":
                coords = [float(coord) for coord in data[1].split()]
                color = tuple(float(c) for c in data[2].split())
                # Create a line source with the loaded coordinates
                line = vtk.vtkLineSource()
                line.SetPoint1(*coords[:3])
                line.SetPoint2(*coords[3:])
                # Create a mapper and actor to render the line
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(line.GetOutputPort())
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the line
                actor.GetProperty().SetColor(color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.line_actor = actor
                # Store the line coordinates and color in class attributes
                self.line_coords = coords
                self.line_color = color
            elif object_type == "polyline":
                coords = [float(coord) for coord in data[1].split()]
                color = tuple(float(c) for c in data[2].split())
                # Create a polyline source with the loaded coordinates
                polyline = vtk.vtkPolyLine()
                for i in range(0, len(coords), 3):
                    polyline.GetPointIds().InsertNextId(i//3)
                    polyline.GetPoints().InsertNextPoint(coords[i:i+3])
                # Create a polydata object and add the polyline to it
                polydata = vtk.vtkPolyData()
                polydata.SetPoints(polyline.GetPoints())
                lines = vtk.vtkCellArray()
                lines.InsertNextCell(polyline)
                polydata.SetLines(lines)
                # Create a mapper and actor to render the polyline
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputData(polydata)
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the polyline
                actor.GetProperty().SetColor(color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.polyline_actor = actor
                # Store the polyline coordinates and color in class attributes
                self.polyline_coords = coords
                self.line_color = color
            elif object_type == "polygon":
                radius, num_sides = [float(x) for x in data[1].split()]
                color = tuple(float(c) for c in data[2].split())
                # Create a regular polygon source with the loaded parameters
                polygon = vtk.vtkRegularPolygonSource()
                polygon.SetNumberOfSides(int(num_sides))
                polygon.SetRadius(radius)
                # Create a mapper and actor to render the polygon
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(polygon.GetOutputPort())
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the polygon
                actor.GetProperty().SetColor(color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.polygon_actor = actor
                # Store the polygon parameters and color in class attributes
                self.polygon_radius = radius
                self.polygon_num_sides = num_sides
                self.line_color = color
            elif object_type == "circle":
                center = [float(x) for x in data[1].split()]
                radius = float(data[2])
                color = tuple(float(c) for c in data[3].split())
                # Create a polygon source with many sides to approximate a circle
                circle_source = vtk.vtkRegularPolygonSource()
                circle_source.SetCenter(center)
                circle_source.SetRadius(radius)
                circle_source.SetNumberOfSides(50)
                # Create a mapper and actor to render the circle
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(circle_source.GetOutputPort())
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the circle
                actor.GetProperty().SetColor(color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.circle_actor = actor
                # Store the circle center, radius, and color in class attributes
                self.circle_center = center
                self.circle_radius = radius
                self.line_color = color
            elif object_type == "arc":
                center = [float(x) for x in data[1].split()]
                radius = float(data[2])
                start_angle = math.radians(float(data[3]))
                end_angle = math.radians(float(data[4]))
                color = tuple(float(c) for c in data[5].split())
                n = int(data[6])
                # Calculate the angle between adjacent vertices
                angle = (end_angle - start_angle) / n
                # Calculate the coordinates of each vertex
                points = vtk.vtkPoints()
                for i in range(n + 1):
                    x = radius * math.cos(start_angle + i * angle)
                    y = radius * math.sin(start_angle + i * angle)
                    points.InsertNextPoint(x, y, 0)
                    # Create the polyline cells
                lines = vtk.vtkCellArray()
                lines.InsertNextCell(n + 1)
                for i in range(n + 1):
                    lines.InsertCellPoint(i)
                    # Create a polydata object and set the points and cells
                polydata = vtk.vtkPolyData()
                polydata.SetPoints(points)
                polydata.SetLines(lines)
                # Create a mapper and actor for the polydata
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputData(polydata)
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the arc
                actor.GetProperty().SetColor(color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.arc_actor = actor
                # Store the arc parameters in a class attribute
                self.arc_params = {"center": center, "radius": radius,
                                   "start_angle": start_angle, "end_angle": end_angle}
            elif object_type == "ellipse":
                center = [float(x) for x in data[1].split()]
                a = float(data[2])
                b = float(data[3])
                n = int(data[4])
                # Calculate the coordinates of each vertex
                points = vtk.vtkPoints()
                for i in range(n + 1):
                    angle = i * (2 * math.pi / n)
                    x = a * math.cos(angle)
                    y = b * math.sin(angle)
                    z = 0
                    points.InsertNextPoint(x, y, z)
                # Create the polyline cells
                lines = vtk.vtkCellArray()
                lines.InsertNextCell(n + 1)
                for i in range(n + 1):
                    lines.InsertCellPoint(i)
                # Create a polydata object and set the points and cells
                polydata = vtk.vtkPolyData()
                polydata.SetPoints(points)
                polydata.SetLines(lines)
                # Create a mapper and actor for the polydata
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputData(polydata)
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the ellipse
                actor.GetProperty().SetColor(self.line_color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.ellipse_actor = actor
                # Store the ellipse parameters in a class attribute
                self.ellipse_params = {"center": center, "a": a, "b": b}
            elif object_type == "sphere":
                params = data[1].rstrip('\n').split()
                center = [float(params[0]), float(params[1]), float(params[2])]
                radius = float(params[3])
                resolution = int(params[4])
                # Create a sphere source with the given parameters
                sphere = vtk.vtkSphereSource()
                sphere.SetRadius(radius)
                sphere.SetCenter(center[0], center[1], center[2])
                sphere.SetThetaResolution(resolution)
                sphere.SetPhiResolution(resolution)
                # Create a mapper and actor to render the sphere
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(sphere.GetOutputPort())
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the sphere
                actor.GetProperty().SetColor(self.line_color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.sphere_actor = actor
                # Store the sphere parameters in class attributes
                self.sphere_radius = radius
                self.sphere_center = center
                self.sphere_resolution = resolution
            elif object_type == "ellipsoid":
                center = [float(x) for x in data[1].split()]
                a = float(data[2])
                b = float(data[3])
                c = float(data[4])
                n = int(data[5])
                # Calculate the coordinates of each vertex
                points = vtk.vtkPoints()
                for i in range(n + 1):
                    theta = i * math.pi / n
                    sin_theta = math.sin(theta)
                    cos_theta = math.cos(theta)
                    for j in range(n + 1):
                        phi = j * 2 * math.pi / n
                        sin_phi = math.sin(phi)
                        cos_phi = math.cos(phi)
                        x = a * sin_theta * cos_phi + center[0]
                        y = b * sin_theta * sin_phi + center[1]
                        z = c * cos_theta + center[2]
                        points.InsertNextPoint(x, y, z)
                # Create a polydata object and set the points
                polydata = vtk.vtkPolyData()
                polydata.SetPoints(points)
                # Create a mapper and actor to render the ellipsoid
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputData(polydata)
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the ellipsoid
                actor.GetProperty().SetColor(self.line_color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.ellipsoid_actor = actor
                # Store the ellipsoid parameters in class attributes
                self.ellipsoid_center = center
                self.ellipsoid_a = a
                self.ellipsoid_b = b
                self.ellipsoid_c = c
                self.ellipsoid_n = n
            elif object_type == "cube":
                center = [float(x) for x in data[1].split()]
                size = float(data[2])
                # Create the cube source
                cube = vtk.vtkCubeSource()
                cube.SetCenter(center)
                cube.SetXLength(size)
                cube.SetYLength(size)
                cube.SetZLength(size)
                # Create a mapper and actor to render the cube
                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(cube.GetOutputPort())
                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                # Set the color of the cube
                actor.GetProperty().SetColor(self.line_color)
                # Add the actor to the renderer and store it in a class attribute
                self.renderer.AddActor(actor)
                self.renderer.ResetCamera()
                self.cube_actor = actor
                # Store the cube parameters in class attributes
                self.cube_center = center
                self.cube_size = size

    def mouse_move_event(self, obj, event):
        # Get the mouse position and convert to display coordinates
        x, y = obj.GetEventPosition()
        display_coords = obj.GetRenderWindow().GetSize()
        display_coords = (display_coords[0], display_coords[1], 1)
        world_coords = obj.GetRenderWindow().GetRenderers(
        ).GetFirstRenderer().SetDisplayPoint(x, y, 0)
        obj.GetRenderWindow().GetRenderers().GetFirstRenderer().DisplayToWorld()
        world_coords = obj.GetRenderWindow().GetRenderers().GetFirstRenderer().GetWorldPoint()
        world_coords = (world_coords[0]/world_coords[3], world_coords[1] /
                        world_coords[3], world_coords[2]/world_coords[3])

        # Update the mouse position labels
        self.x_label.setText("{:.2f}".format(world_coords[0]))
        self.y_label.setText("{:.2f}".format(world_coords[1]))

    def draw_polygon(self):
        # Ask the user for polygon parameters
        num_sides, ok1 = QInputDialog.getInt(
            self, "Enter number of sides", "Number of sides:", 3, 3, 100)
        radius, ok2 = QInputDialog.getDouble(
            self, "Enter radius", "Radius:", 1.0, 0.1, 100.0)
        alpha, ok3 = QInputDialog.getDouble(
            self, "Enter alpha", "Alpha (in radians):", 0.0, 0.0, 2 * math.pi)
        cx, ok4 = QInputDialog.getDouble(
            self, "Enter x-coordinate of center", "X-coordinate of center:", 0.0, -100.0, 100.0)
        cy, ok5 = QInputDialog.getDouble(
            self, "Enter y-coordinate of center", "Y-coordinate of center:", 0.0, -100.0, 100.0)

        if not (ok1 and ok2 and ok3 and ok4 and ok5):
            return

         # Calculate the vertices of the polygon using the given equation
        points = vtk.vtkPoints()
        for i in range(num_sides):
            x = radius * math.cos(2 * math.pi * i / num_sides + alpha) + cx
            y = radius * math.sin(2 * math.pi * i / num_sides + alpha) + cy
            z = 0.0
            points.InsertNextPoint(x, y, z)

        # Create a polygon source from the calculated points
        polygon = vtk.vtkPolygon()
        polygon.GetPointIds().SetNumberOfIds(num_sides)
        for i in range(num_sides):
            polygon.GetPointIds().SetId(i, i)

        polygon_polydata = vtk.vtkPolyData()
        polygon_polydata.Allocate(1, 1)
        polygon_polydata.InsertNextCell(
        polygon.GetCellType(), polygon.GetPointIds())
        polygon_polydata.SetPoints(points)

        # Create a mapper and actor to render the polygon
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polygon_polydata)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the polygon
        actor.GetProperty().SetColor(self.line_color)

    # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the polygon actor in a class attribute
        self.polygon_actor = actor

    # Store the polygon parameters in class attributes
        self.polygon_num_sides = num_sides
        self.polygon_radius = radius
        self.polygon_alpha = alpha
        self.polygon_cx = cx
        self.polygon_cy = cy

    # Set up mouse event handling
        self.interactor.AddObserver(
            "MouseMoveEvent", self.polygon_mouse_move_event)
        self.interactor.AddObserver(
            "LeftButtonReleaseEvent", self.polygon_mouse_release_event)

    # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    def polygon_mouse_move_event(self, obj, event):
        if not self.polygon_actor:
            return

        # Get the current mouse position
        pos = self.interactor.GetEventPosition()

        # Calculate the displacement of the mouse
        dx = pos[0] - self.polygon_mouse_pos[0]
        dy = pos[1] - self.polygon_mouse_pos[1]

        # Convert the initial position of the polygon to display coordinates
        display_pos = vtk.vtkVector3d()
        self.renderer.WorldToDisplay(self.polygon_initial_pos, display_pos)

        # Move the polygon to the new position
        new_display_pos = vtk.vtkVector3d(
        display_pos[0] + dx, display_pos[1] + dy, 0)
        new_world_pos = vtk.vtkVector3d()
        self.renderer.DisplayToWorld(new_display_pos, new_world_pos)
        self.polygon_actor.SetPosition(new_world_pos)

    def polygon_mouse_release_event(self, obj, event):
        if not self.polygon_actor:
            return

        # Calculate the vertices of the polygon
        num_sides = self.num_sides_spin_box.value()
        center = self.polygon_actor.GetPosition()
        radius = vtk.vtkMath.Distance2D(
            center[:2], self.polygon_initial_pos[:2])
        angle = 2 * vtk.vtkMath.DoublePi() / num_sides
        vertices = []
        for i in range(num_sides):
            x = center[0] + radius * math.cos(i * angle)
            y = center[1] + radius * math.sin(i * angle)
            z = center[2]
            vertices.append((x, y, z))

        # Create the polygon source and mapper
        polygon = vtk.vtkPolygon()
        polygon.GetPoints().SetData(vtk.vtkFloatArray().FromArray(vertices, num_sides, 3))
        polygon_mapper = vtk.vtkPolyDataMapper()
        polygon_mapper.SetInputData(polygon)

        # Set the actor properties
        self.polygon_actor.SetMapper(polygon_mapper)
        self.polygon_actor.GetProperty().SetColor(self.color_picker.color)
        self.polygon_actor.GetProperty().SetOpacity(self.opacity_slider.value())

        # Add the polygon actor to the renderer
        self.renderer.AddActor(self.polygon_actor)
        self.interactor.Render()

        # Reset the polygon actor and mouse position variables
        self.polygon_actor = None
        self.polygon_initial_pos = None
        self.polygon_mouse_pos = None

    def draw_circle(self):
        # Ask the user for the circle center and radius
        center, ok1_pressed = QInputDialog.getText(
            self, "Enter circle center", "x y z", QtWidgets.QLineEdit.Normal, "0 0 0")
        if not ok1_pressed:
            return
        radius, ok2_pressed = QInputDialog.getDouble(
            self, "Enter circle radius", "Radius", 1, 0, 1000, 2)
        if not ok2_pressed:
            return

        # Convert the center string to a list of floats
        center_list = list(map(float, center.split()))

        # Create a polygon source with many sides to approximate a circle
        circle_source = vtk.vtkRegularPolygonSource()
        circle_source.SetCenter(center_list)
        circle_source.SetRadius(radius)
        circle_source.SetNumberOfSides(50)

        # Create a mapper and actor to render the circle
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(circle_source.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the circle
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.circle_actor = actor

        # Create a cell picker and set its tolerance (in pixels)
        picker = vtk.vtkCellPicker()
        picker.SetTolerance(0.01)

        # Get the x, y screen position of the mouse click
        x, y = self.interactor.GetEventPosition()

        # Pick from the center of the screen
        picker.Pick(x, y, 0, self.renderer)

        # Get the picked actor and cell
        actor = picker.GetActor()
        cell = picker.GetCellId()

        # If an actor and cell were picked, do something
        if actor and cell >= 0:
            # Do something with the picked actor and cell
            pass

    def Shear_Circle(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.circle_actor:
            # Get the current position of the circle
            current_position = self.circle_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.circle_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.circle_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def draw_arc(self):
        # Ask the user for arc parameters
        center, ok_pressed = QInputDialog.getText(
            self, "Enter arc center", "x y z", QtWidgets.QLineEdit.Normal, "0 0 0")
        if not ok_pressed:
            return
        radius, ok_pressed = QInputDialog.getDouble(
            self, "Enter arc radius", "Radius", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return
        start_angle, ok_pressed = QInputDialog.getDouble(
            self, "Enter arc start angle", "Start Angle (degrees)", 0.0, -360.0, 360.0, 2)
        if not ok_pressed:
            return
        end_angle, ok_pressed = QInputDialog.getDouble(
            self, "Enter arc end angle", "End Angle (degrees)", 90.0, -360.0, 360.0, 2)
        if not ok_pressed:
            return
        n, ok_pressed = QInputDialog.getInt(
            self, "Enter number of points", "Number of points", 10, 1, 1000, 1)
        if not ok_pressed:
            return

        # Convert the angles to radians
        start_angle = math.radians(start_angle)
        end_angle = math.radians(end_angle)

        # Calculate the angle between adjacent vertices
        angle = (end_angle - start_angle) / n

        # Calculate the coordinates of each vertex
        points = vtk.vtkPoints()
        for i in range(n + 1):
            x = radius * math.cos(start_angle + i * angle)
            y = radius * math.sin(start_angle + i * angle)
            points.InsertNextPoint(x, y, 0)

        # Create the polyline cells
        lines = vtk.vtkCellArray()
        lines.InsertNextCell(n + 1)
        for i in range(n + 1):
            lines.InsertCellPoint(i)

        # Create a polydata object and set the points and cells
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetLines(lines)

        # Create a mapper and actor for the polydata
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the arc
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the arc actor in a class attribute
        self.arc_actor = actor

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

        # Store the arc parameters in a class attribute
        self.arc_params = {"center": list(map(float, center.split(
        ))), "radius": radius, "start_angle": start_angle, "end_angle": end_angle}

    def draw_irr_polygon(self):
        # Ask the user for polygon parameters
        coordinates, ok_pressed = QInputDialog.getText(
            self, "Enter polygon coordinates", "x1 y1 z1 x2 y2 z2 ... xn yn zn", QtWidgets.QLineEdit.Normal, "0 0 0 1 1 1 2 2 2")
        if not ok_pressed:
            return
        coordinates_list = coordinates.split()
        if len(coordinates_list) % 3 != 0:
            return

        n = len(coordinates_list) // 3

        # Calculate the coordinates of each vertex
        points = vtk.vtkPoints()
        for i in range(n):
            x = float(coordinates_list[i * 3])
            y = float(coordinates_list[i * 3 + 1])
            z = float(coordinates_list[i * 3 + 2])
            points.InsertNextPoint(x, y, z)

        # Create the polygon cells
        cells = vtk.vtkCellArray()
        cells.InsertNextCell(n)
        for i in range(n):
            cells.InsertCellPoint(i)

        # Create a polydata object and set the points and cells
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetPolys(cells)

        # Create a mapper and actor for the polydata
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the polygon
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the polygon actor in a class attribute
        self.irr_polygon_actor = actor

        # Store the polygon parameters in a class attribute
        self.polygon_params = {"coordinates": list(
            map(float, coordinates_list))}

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    def draw_ellipse(self):
        # Ask the user for ellipse parameters
        center, ok_pressed = QInputDialog.getText(
            self, "Enter ellipse center", "x y z", QtWidgets.QLineEdit.Normal, "0 0 0")
        if not ok_pressed:
            return
        a, ok_pressed = QInputDialog.getDouble(
            self, "Enter ellipse half-width", "a", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return
        b, ok_pressed = QInputDialog.getDouble(
            self, "Enter ellipse half-height", "b", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return
        n, ok_pressed = QInputDialog.getInt(
            self, "Enter number of points", "Number of points", 10, 1, 1000, 1)
        if not ok_pressed:
            return

        # Calculate the coordinates of each vertex
        points = vtk.vtkPoints()
        for i in range(n + 1):
            angle = i * (2 * math.pi / n)
            x = a * math.cos(angle)
            y = b * math.sin(angle)
            z = 0
            points.InsertNextPoint(x, y, z)

        # Create the polyline cells
        lines = vtk.vtkCellArray()
        lines.InsertNextCell(n + 1)
        for i in range(n + 1):
            lines.InsertCellPoint(i)

        # Create a polydata object and set the points and cells
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetLines(lines)

        # Create a mapper and actor for the polydata
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the ellipse
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the ellipse actor in a class attribute
        self.ellipse_actor = actor

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

        # Store the ellipse parameters in a class attribute
        self.ellipse_params = {"center": list(
            map(float, center.split())), "a": a, "b": b}

    def Translate_line(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.line_actor:

            # Get the current position of the line
            current_position = self.line_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.line_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_polyline(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.polyline_actor:

            # Get the current position of the line
            current_position = self.polyline_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.polyline_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_polygon(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.polygon_actor:

            # Get the current position of the line
            current_position = self.polygon_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.polygon_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_Circle(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        if current_actor == self.circle_actor:

            current_position = self.circle_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                self.circle_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return
        else:
            return "Please enter a valid shape"

    def Translate_arc(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.arc_actor:

            # Get the current position of the line
            current_position = self.arc_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.arc_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_irr_polygon(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.irr_polygon_actor:

            # Get the current position of the line
            current_position = self.irr_polygon_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.irr_polygon_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_ellipse(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.ellipse_actor:

            # Get the current position of the line
            current_position = self.ellipse_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.ellipse_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_Sphere(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.sphere_actor:

            # Get the current position of the line
            current_position = self.sphere_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.sphere_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_Ellipsoid(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.ellipsoid_actor:

            # Get the current position of the line
            current_position = self.ellipsoid_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.ellipsoid_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def Translate_Cube(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a line actor
        if current_actor == self.cube_actor:

            # Get the current position of the line
            current_position = self.cube_actor.GetPosition()

            # Ask the user for the translation distance
            translation_distance, ok = QInputDialog.getDouble(self, "Translation Distance",
                                                              "Enter translation distance:")
            if ok:
                # Calculate the new position of the line
                new_position = (current_position[0] + translation_distance,
                                current_position[1] + translation_distance,
                                current_position[2])

                # Update the position of the line actor
                self.cube_actor.SetPosition(new_position)

                # Render the scene
                self.vtk_widget.GetRenderWindow().Render()
                return

    def onScaleClicked(self):
        # Get the current actor
        actor = self.renderer.GetActors().GetLastActor()

        # Ask the user for the scaling factor
        scale, ok_pressed = QInputDialog.getDouble(
            self, "Scale Actor", "Scaling Factor:", 1, 0, 100, 2)
        if not ok_pressed:
            return

        # Get the current scale of the actor
        current_scale = actor.GetScale()

        # Calculate the new scale factor based on the user input and the current scale
        new_scale = (
            scale * current_scale[0], scale * current_scale[1], scale * current_scale[2])

        # Set the new scale on the actor
        actor.SetScale(new_scale)

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    def draw_sphere(self):
        # Ask the user for sphere parameters
        radius, ok1 = QInputDialog.getDouble(
            self, "Enter radius", "Radius:", 1.0, 0.1, 100.0)
        center_x, ok2 = QInputDialog.getDouble(
            self, "Enter x-coordinate for center", "Center x-coordinate:", 0.0, -100.0, 100.0)
        center_y, ok3 = QInputDialog.getDouble(
            self, "Enter y-coordinate for center", "Center y-coordinate:", 0.0, -100.0, 100.0)
        center_z, ok4 = QInputDialog.getDouble(
            self, "Enter z-coordinate for center", "Center z-coordinate:", 0.0, -100.0, 100.0)
        resolution, ok5 = QInputDialog.getInt(
            self, "Enter resolution", "Resolution:", 16, 3, 100)
        if not ok1 or not ok2 or not ok3 or not ok4 or not ok5:
            return

        # Create a sphere source with the given parameters
        sphere = vtk.vtkSphereSource()
        sphere.SetRadius(radius)
        sphere.SetCenter(center_x, center_y, center_z)
        sphere.SetThetaResolution(resolution)
        sphere.SetPhiResolution(resolution)

        # Create a mapper and actor to render the sphere
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the sphere
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        # Store the sphere actor in a class attribute
        self.sphere_actor = actor

        # Store the sphere parameters in class attributes
        self.sphere_radius = radius
        self.sphere_center = (center_x, center_y, center_z)
        self.sphere_resolution = resolution

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    def draw_ellipsoid(self):
        # Ask the user for ellipsoid parameters
        center, ok_pressed = QInputDialog.getText(
            self, "Enter ellipsoid center", "x y z", QtWidgets.QLineEdit.Normal, "0 0 0")
        if not ok_pressed:
            return
        a, ok_pressed = QInputDialog.getDouble(
            self, "Enter ellipsoid semi-axis length a", "a", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return
        b, ok_pressed = QInputDialog.getDouble(
            self, "Enter ellipsoid semi-axis length b", "b", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return
        c, ok_pressed = QInputDialog.getDouble(
            self, "Enter ellipsoid semi-axis length c", "c", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return
        n, ok_pressed = QInputDialog.getInt(
            self, "Enter number of points", "Number of points", 50, 1, 1000, 1)
        if not ok_pressed:
            return

        # Calculate the coordinates of each vertex
        points = vtk.vtkPoints()
        for i in range(n + 1):
            theta = i * math.pi / n
            sin_theta = math.sin(theta)
            cos_theta = math.cos(theta)
            for j in range(n + 1):
                phi = j * 2 * math.pi / n
                sin_phi = math.sin(phi)
                cos_phi = math.cos(phi)
                x = a * sin_theta * cos_phi
                y = b * sin_theta * sin_phi
                z = c * cos_theta
                points.InsertNextPoint(x, y, z)

    # Create the triangle cells
        triangles = vtk.vtkCellArray()
        for i in range(n):
            for j in range(n):
                p1 = i * (n + 1) + j
                p2 = p1 + (n + 1)
                triangles.InsertNextCell(3)
                triangles.InsertCellPoint(p1)
                triangles.InsertCellPoint(p2)
                triangles.InsertCellPoint(p1 + 1)

                triangles.InsertNextCell(3)
                triangles.InsertCellPoint(p1 + 1)
                triangles.InsertCellPoint(p2)
                triangles.InsertCellPoint(p2 + 1)

        # Create a polydata object and set the points and cells
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetPolys(triangles)

    # Create a mapper and actor for the polydata
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the ellipsoid
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

    # Store the ellipsoid actor in a class attribute
        self.ellipsoid_actor = actor

    # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    # Store the ellipsoid parameters in a class attribute
        self.ellipsoid_params = {"center": list(
            map(float, center.split())), "a": a, "b": b, "c": c}

    def draw_cube(self):
        # Ask the user for cube parameters
        center, ok_pressed = QInputDialog.getText(
            self, "Enter cube center", "x y z", QtWidgets.QLineEdit.Normal, "0 0 0")
        if not ok_pressed:
            return
        size, ok_pressed = QInputDialog.getDouble(
            self, "Enter cube size", "Size:", 1.0, 0.1, 100.0, 2)
        if not ok_pressed:
            return

        # Create the cube source
        cube = vtk.vtkCubeSource()
        cube.SetCenter(list(map(float, center.split())))
        cube.SetXLength(size)
        cube.SetYLength(size)
        cube.SetZLength(size)

        # Create a mapper and actor to render the cube
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(cube.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Set the color of the cube
        actor.GetProperty().SetColor(self.line_color)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)

        # Store the cube actor in a class attribute
        self.cube_actor = actor

        # Store the cube parameters in a class attribute
        self.cube_center = list(map(float, center.split()))
        self.cube_size = size

        # Render the scene
        self.vtk_widget.GetRenderWindow().Render()

    def Shear_line(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.line_actor:
            # Get the current position of the circle
            current_position = self.line_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.line_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.line_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Polyline(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.polyline_actor:
            # Get the current position of the circle
            current_position = self.polyline_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.polyline_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.polyline_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Polygon(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.polygon_actor:
            # Get the current position of the circle
            current_position = self.polygon_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.polygon_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.polygon_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_irr_polygon(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.irr_polygon_actor:
            # Get the current position of the circle
            current_position = self.irr_polygon_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.irr_polygon_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.irr_polygon_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Ellipse(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.ellipse_actor:
            # Get the current position of the circle
            current_position = self.ellipse_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.ellipse_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.ellipse_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Arc(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.arc_actor:
            # Get the current position of the circle
            current_position = self.arc_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.arc_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.arc_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Circle(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.circle_actor:
            # Get the current position of the circle
            current_position = self.circle_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.circle_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.circle_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Sphere(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.sphere_actor:
            # Get the current position of the circle
            current_position = self.sphere_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.sphere_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.sphere_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Cube(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.cube_actor:
            # Get the current position of the circle
            current_position = self.cube_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.cube_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.cube_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return

    def Shear_Ellipsoid(self):
        current_actor = self.renderer.GetActors().GetLastActor()
        # Check if the selected actor is a circle actor
        if current_actor == self.ellipsoid_actor:
            # Get the current position of the circle
            current_position = self.ellipsoid_actor.GetPosition()

            # Ask the user for the shear amount
            shear_factor, ok = QInputDialog.getDouble(self, "Shear Amount",
                                                      "Enter shear amount:")
            if ok:
                # Calculate the new position of the circle
                new_vertices = vtk.vtkPoints()
                original_vertices = self.ellipsoid_actor.GetMapper().GetInput().GetPoints()
                num_vertices = original_vertices.GetNumberOfPoints()
                for i in range(num_vertices):
                    x, y, z = original_vertices.GetPoint(i)
                    new_vertices.InsertNextPoint(x + y * shear_factor, y, z)

            # Update the position of the circle actor
            self.ellipsoid_actor.GetMapper().GetInput().SetPoints(new_vertices)

            # Render the scene
            self.vtk_widget.GetRenderWindow().Render()
        return


if __name__ == "__main__":
    # Create a PyQt application
    # Create a main window and run the application
    app = QtWidgets.QApplication([])
    window = MyRenderWindow()
    app.exec_()
