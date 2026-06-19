window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('three-canvas');
    if (!canvas) return;

    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);

    const scene = new THREE.Scene();
    
    // Setup camera
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 0, 8); 

    // Setup lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(5, 10, 7);
    scene.add(dirLight);

    const pointLight = new THREE.PointLight(0xffaa00, 1, 100);
    pointLight.position.set(-5, 5, -5);
    scene.add(pointLight);

    let model = null;
    let baseScale = 1;

    // Load model
    const loader = new THREE.GLTFLoader();
    loader.load('/color_palette/scene.gltf', (gltf) => {
        model = gltf.scene;
        
        // Center the model's geometry
        const box = new THREE.Box3().setFromObject(model);
        const center = box.getCenter(new THREE.Vector3());
        model.position.set(-center.x, -center.y, -center.z);
        
        // Wrapper for easier pivoting
        const wrapper = new THREE.Group();
        wrapper.add(model);
        scene.add(wrapper);
        model = wrapper; // animate the wrapper
        
        // Rotate to a nice initial angle
        model.rotation.x = Math.PI / 6;
        model.rotation.y = -Math.PI / 6;
        
        // Auto-adjust scale based on bounding box
        const size = box.getSize(new THREE.Vector3());
        const maxDim = Math.max(size.x, size.y, size.z);
        const desiredSize = 1.8; // Much smaller to fit in the UI without blocking
        baseScale = desiredSize / maxDim;
        model.scale.setScalar(baseScale);

        setupScrollAnimations(model, baseScale);

    }, undefined, (error) => {
        console.error('Error loading GLTF:', error);
    });

    function setupScrollAnimations(target, scale) {
        if (!window.gsap || !window.ScrollTrigger) return;
        gsap.registerPlugin(ScrollTrigger);

        // 1. AI Section: Timeline for multiple scrolls
        const aiTl = gsap.timeline({
            scrollTrigger: {
                trigger: "#ai",
                start: "top 80%",
                end: "center center",
                scrub: 1
            }
        });
        
        // Step 1: Move to right (2nd scroll)
        aiTl.to(target.position, {
            x: 2.5,
            y: 0.5,
            z: -2,
            duration: 1,
            ease: "power2.inOut"
        }, 0);
        aiTl.to(target.rotation, {
            x: Math.PI / 2,
            y: Math.PI,
            duration: 1,
            ease: "power2.inOut"
        }, 0);

        // Step 2: Move back to center and scale up (3rd scroll)
        aiTl.to(target.position, {
            x: 0,
            y: -0.5,
            z: 2,
            duration: 1.5,
            ease: "power2.inOut"
        }, 1.5);
        aiTl.to(target.rotation, {
            x: Math.PI / 4,
            y: Math.PI * 2,
            z: 0,
            duration: 1.5,
            ease: "power2.inOut"
        }, 1.5);

        // 2. Features Section: Move to the left
        gsap.to(target.position, {
            x: -2.5,
            y: 0,
            z: -1,
            ease: "power1.inOut",
            scrollTrigger: {
                trigger: "#features",
                start: "top center",
                end: "bottom center",
                scrub: 1
            }
        });
        gsap.to(target.rotation, {
            x: 0,
            y: Math.PI * 2,
            z: Math.PI / 4,
            ease: "power1.inOut",
            scrollTrigger: {
                trigger: "#features",
                start: "top center",
                end: "bottom center",
                scrub: 1
            }
        });

        // 3. Encryption Section: Move to center bottom
        gsap.to(target.position, {
            x: 0,
            y: -1.5,
            z: 1,
            ease: "power2.out",
            scrollTrigger: {
                trigger: "#encryption",
                start: "top 70%",
                end: "center center",
                scrub: 1
            }
        });

        // 4. Grip Section: Move to left and scale up
        gsap.to(target.position, {
            x: -2,
            y: 0,
            z: 2,
            ease: "power2.inOut",
            scrollTrigger: {
                trigger: "#grip",
                start: "top 80%",
                end: "center center",
                scrub: 1
            }
        });
        gsap.to(target.scale, {
            x: scale * 1.5,
            y: scale * 1.5,
            z: scale * 1.5,
            ease: "power2.inOut",
            scrollTrigger: {
                trigger: "#grip",
                start: "top 80%",
                end: "center center",
                scrub: 1
            }
        });
    }

    // Handle scroll to rotate slightly continuously
    window.addEventListener('scroll', () => {
        if (model && !window.gsap) {
            // Fallback if GSAP fails
            const scrollY = window.scrollY;
            model.rotation.y = -Math.PI / 6 + scrollY * 0.002;
        }
    });

    const clock = new THREE.Clock();

    // Handle resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // Animation loop
    const animate = () => {
        requestAnimationFrame(animate);
        if (model) {
            const elapsedTime = clock.getElapsedTime();
            // Add a very subtle float on top of the GSAP animation
            model.position.y += Math.sin(elapsedTime * 2) * 0.001; 
        }
        renderer.render(scene, camera);
    };
    animate();
});
